import hashlib
import hmac
import logging
import os
import sys
import time
from dataclasses import dataclass, field
from getpass import getpass


# ---------------------------------------------------------------------------
# Configuração de logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("autenticacao.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------

@dataclass
class ConfigAuth:
    """Parâmetros de comportamento do autenticador."""
    max_tentativas: int = 5
    penalidade_base_segundos: int = 2
    penalidade_maxima_segundos: int = 30
    # Lê o hash de uma variável de ambiente; nunca hardcode no fonte.
    # Para gerar: python -c "import hashlib; print(hashlib.sha256('suasenha'.encode()).hexdigest())"
    hash_esperado: str = field(
        default_factory=lambda: os.environ.get("AUTH_HASH_ESPERADO", "")
    )

    def __post_init__(self) -> None:
        if not self.hash_esperado:
            raise EnvironmentError(
                "Variável de ambiente AUTH_HASH_ESPERADO não definida.\n"
                "Gere o hash com:\n"
                "  python -c \"import hashlib; print(hashlib.sha256('suasenha'.encode()).hexdigest())\"\n"
                "E exporte-o antes de rodar (exemplos):\n"
                "  export AUTH_HASH_ESPERADO=<hash>              # Linux / macOS\n"
                "  setx AUTH_HASH_ESPERADO <hash>               # Windows CMD (novo terminal)\n"
                "  $env:AUTH_HASH_ESPERADO = '<hash>'           # PowerShell (sessão atual)"
            )


# ---------------------------------------------------------------------------
# Utilitários criptográficos
# ---------------------------------------------------------------------------

def gerar_hash(texto: str) -> str:
    """Normaliza e retorna o SHA-256 do texto."""
    texto_limpo = texto.strip().lower()
    return hashlib.sha256(texto_limpo.encode("utf-8")).hexdigest()


def comparar_hashes(hash_a: str, hash_b: str) -> bool:
    """Compara hashes em tempo constante para evitar timing attacks."""
    return hmac.compare_digest(hash_a, hash_b)


# ---------------------------------------------------------------------------
# Estado de autenticação
# ---------------------------------------------------------------------------

@dataclass
class EstadoAuth:
    """Mantém o estado da sessão de autenticação."""
    tentativas: int = 0
    bloqueado_ate: float = 0.0

    @property
    def esta_bloqueado(self) -> bool:
        return time.monotonic() < self.bloqueado_ate

    @property
    def segundos_restantes(self) -> int:
        return max(0, int(self.bloqueado_ate - time.monotonic()))

    def registrar_falha(self, penalidade_base: int, penalidade_maxima: int) -> None:
        self.tentativas += 1
        penalidade = min(self.tentativas * penalidade_base, penalidade_maxima)
        self.bloqueado_ate = time.monotonic() + penalidade

    def tentativas_esgotadas(self, max_tentativas: int) -> bool:
        return self.tentativas >= max_tentativas


# ---------------------------------------------------------------------------
# Autenticador
# ---------------------------------------------------------------------------

class Autenticador:
    """Gerencia o fluxo de autenticação de forma segura."""

    def __init__(self, config: ConfigAuth) -> None:
        self._config = config

    def _aguardar_bloqueio(self, estado: EstadoAuth) -> None:
        """Espera ativamente, exibindo contagem regressiva."""
        while estado.esta_bloqueado:
            restante = estado.segundos_restantes
            print(f"\r⏳ Aguarde {restante}s para tentar novamente...   ", end="", flush=True)
            time.sleep(1)
        print()  # quebra de linha após contagem

    def autenticar(self) -> bool:
        """
        Executa o fluxo de login.
        Retorna True em caso de sucesso, False em caso de falha ou interrupção.
        """
        estado = EstadoAuth()
        cfg = self._config

        self._exibir_cabecalho()

        while not estado.tentativas_esgotadas(cfg.max_tentativas):
            # Aguarda caso esteja bloqueado
            if estado.esta_bloqueado:
                self._aguardar_bloqueio(estado)

            try:
                entrada = getpass("Chave de Acesso: ")
            except (KeyboardInterrupt, EOFError):
                print("\n\n🚨 Sessão encerrada pelo usuário.")
                logger.warning("Sessão encerrada via interrupção do usuário.")
                return False

            if comparar_hashes(gerar_hash(entrada), cfg.hash_esperado):
                logger.info("Acesso autorizado.")
                print("\n🔓 [SUCESSO] Acesso liberado.\n")
                return True

            estado.registrar_falha(cfg.penalidade_base_segundos, cfg.penalidade_maxima_segundos)
            tentativas_restantes = cfg.max_tentativas - estado.tentativas

            logger.warning(
                "Falha de autenticação #%d. Tentativas restantes: %d.",
                estado.tentativas,
                tentativas_restantes,
            )
            print(
                f"\n❌ Chave incorreta. "
                f"Tentativas restantes: {tentativas_restantes}."
            )

        logger.error("Limite de tentativas atingido. Acesso bloqueado permanentemente nesta sessão.")
        print("\n🔒 Número máximo de tentativas atingido. Sessão encerrada.\n")
        return False

    @staticmethod
    def _exibir_cabecalho() -> None:
        print("\n" + "=" * 45)
        print("   SISTEMA DE AUTENTICAÇÃO CRIPTOGRAFADO")
        print("=" * 45 + "\n")


# ---------------------------------------------------------------------------
# Ponto de entrada
# ---------------------------------------------------------------------------

def main() -> None:
    try:
        config = ConfigAuth()
    except EnvironmentError as erro:
        print(f"\n⚠️  Erro de configuração:\n{erro}\n")
        sys.exit(1)

    autenticador = Autenticador(config)
    sucesso = autenticador.autenticar()
    sys.exit(0 if sucesso else 1)


if __name__ == "__main__":
    main()

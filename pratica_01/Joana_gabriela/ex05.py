tam_arquivo = float(input("Tamanho do arquivo em MB: \n"))
vel_internet = float(input("Velocidade de internet (Mpbs): \n"))

temp_seg = tam_arquivo / (vel_internet/8)
min_inteiro = temp_seg // 60
segundos_rest = temp_seg % 60

print(f"Tempo estimado: {min_inteiro:.0f}m {segundos_rest:.0f}s")
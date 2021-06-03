
cmd_principal = "git"
# cmd_secundario = "clone" # commit, clone, reset, status
cmd_secundario = input()
print(type(cmd_secundario))

if cmd_principal == "git":
    if cmd_secundario == "add":
        print("Archivos agregados")
    elif cmd_secundario == "commit":
        print("Se guardaron los cambios")
    elif cmd_secundario == "clone":
        print("Clono el repo remoto")
    elif cmd_secundario == "reset":
        print("Vuelvo para atras")
    else:
        print("Comando no valido")
else:
    print("Comando no valido")





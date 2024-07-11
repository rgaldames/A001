from funciones import Menu, AgregarBono, ListasBonos

def main():
    while True:
        op=Menu()
        if op=="5":
            print("  Chao  !!!!")
            break

        if op=="1":
            AgregarBono()

        elif op=="2":
            ListasBonos()
        

if __name__=='__main__':
    main()

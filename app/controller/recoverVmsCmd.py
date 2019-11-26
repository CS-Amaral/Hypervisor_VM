import subprocess

class Get_vms():
    def __init__(self):
        self.listaLimpa = []
        self.vm = ""
        self.listinha = ""
        


    def recoverVMS(self):
        #Sprint("AS")
        processo = str(subprocess.check_output("VBoxManage list vms"))
        listaDeVms = processo.split('\\r\\n')
        #listaLimpa = []
        #Trantando a String vinda do CMD
        for vms in listaDeVms:
            vm = vms
            if len(vm) < 2:
                continue
            elif "b'" in vm:
                vm = vm.replace("b'", '')
                listinha = vm.split(" ")
                limpinho = self.tratandoString(listinha[0])
                #print("sa")
                
            else:
                listinha = vm.split(" ")
                limpinho = self.tratandoString(listinha[0])
                
        #print(self.listaLimpa)
        return self.listaLimpa

    def tratandoString(self, termo):
        vm = termo.replace('"', '')
        self.listaLimpa.append(str(vm))

    
#a = Get_vms()
#k = a.recoverVMS()
#print(k)


    
    

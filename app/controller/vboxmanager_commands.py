from app.controller.recoverVmsCmd import Get_vms
import subprocess

class Change_vm():
    
    def __init__(self,tipo,cpu,qtdMemoria,ip):
        self.comando = ""
        self.get_vm = Get_vms()
        self.tipo = int(tipo)
        self.cpu = cpu
        self.qtdMemoria = qtdMemoria
        self.ip = ip

    
    def clonarVm(self):
        print("Clonando VM...")
        if self.tipo == 0:
            vm = "windowns7start"
        else:
            vm = "ubuntu"
        novaVm = self.nomearVm()
        comando = subprocess.check_output("VBoxManage clonevm " + vm + " --name " + novaVm + " --register")
        self.modificacoesDoUsuario(novaVm)
        self.configuracoesIP()
        print ("VM Criada com Sucesso | Nome da VM: " + novaVm)
        return novaVm


    def nomearVm(self):
        listaVMS = self.get_vm.recoverVMS()
        #print(listaVMS)
        if self.tipo == 0:
            for i in range(100):
                nomevm = "win7start_clone_" + str(i)
                #print(nomevm)
                if nomevm not in listaVMS:
                    break
        else:
            for i in range(100):
                nomevm = "ubuntu_clone_" + str(i)
                if nomevm not in listaVMS:
                    break
        
        
        return nomevm
    
    def modificacoesDoUsuario(self,nomevm):
        print("Modificando quantidade de Memoria...")
        #Memoria
        subprocess.check_output("VBoxManage modifyvm " + nomevm + " --memory " + self.qtdMemoria)
        print("Modificando quantidade de CPU ...")
        #CPU --cpus <number>
        subprocess.check_output("VBoxManage modifyvm " + nomevm + " --cpus " + self.cpu)

        
    def configuracoesIP(self):
        print("Configurando IP da Rede ...")

        listadeIps = self.validacaoIP()
        #IP
        #Setp1 Verificando o IP do Adaptador
        subprocess.check_output('vboxmanage.exe hostonlyif ipconfig "VirtualBox Host-Only Ethernet Adapter #3" --ip 169.254.167.246 --netmask 255.255.255.0')

        #Setp2 Removendo o servidor DHCP
        subprocess.check_output('vboxmanage.exe dhcpserver remove --ifname "VirtualBox Host-Only Ethernet Adapter #3"')

        #Step3 Adicionando novo servidor DHCP
        subprocess.check_output('vboxmanage.exe dhcpserver add --ifname "VirtualBox Host-Only Ethernet Adapter #3" --ip ' + listadeIps[0] + ' --netmask 255.255.255.0 --lowerip ' + listadeIps[1] + ' --upperip ' + listadeIps[1] + ' --enable')


    def validacaoIP(self):
        stringIP = ""
        ipsConfig = []
        ipTestestr = self.ip
        ipTeste = ipTestestr.split(".")
        ultimodigito = ipTeste[len(ipTeste)-1]
        if int(ultimodigito) > 0:
            for i in range(len(ipTeste)):
                if i+1 != len(ipTeste):
                    stringIP+=str(ipTeste[i]) + "."
                else:
                    valorFinalIp = int(ipTeste[i]) - 1
                    stringIP+=str(valorFinalIp)
            
            ipsConfig.append(stringIP)
            ipsConfig.append(ipTestestr)
            #print(ipsConfig)
            return ipsConfig
        else:
            ipsConfig.append(ipTestestr)
            for i in range(len(ipTeste)):
                if i+1 != len(ipTeste):
                    stringIP+=str(ipTeste[i]) + "."
                else:
                    valorFinalIp = int(ipTeste[i]) + 1
                    stringIP+=str(valorFinalIp)
            ipsConfig.append(stringIP)
            #print(ipsConfig)
            return ipsConfig


                
            


        

    #VBoxManage modifyvm "cloneubuntu 1" --memory 1024

#cvm = Change_vm("0","2","512","192.168.56.12")
#cvm.clonarVm()
#cvm.validacaoIP()





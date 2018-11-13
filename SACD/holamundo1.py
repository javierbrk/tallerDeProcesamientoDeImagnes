import reco_patron.algoritmo2 as alg
import dbmanage.da_mysql as mysql



TB_Dispositivo = mysql.formato_tabla('sacd_dispositivos')

TB_Dispositivo.add_fiel('SDisModelo')
TB_Dispositivo.add_key('SDisCod')

resp = mysql._SQLexec(TB_Dispositivo.read_last()).fetchall()

print(TB_Dispositivo.read_last())
print(resp)



TB_Dispositivo.clean()
TB_Dispositivo.add_fiel("SDisCod, SDisStatus, SDisEmpresa, SDisID, SDisModelo, SDisSerie, SDisMarca, SDisObser, SDisFechCre, SDisUserCre")
print(TB_Dispositivo.insert()%('',1, 'AGUA', 'PRU45', 'TESTO470', '789654', 'TESTO', 'N/A', '2018-8-15', 'CS'))

mysql._SQLexec(TB_Dispositivo.insert()%('',1, 'TIERRA', 'PRUB78', 'TESTO4_70', '789654', 'TESTO', 'N/A', '2018-8-15', 'CS'))


mysql._SQLclose

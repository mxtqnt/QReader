# QReader

Código em Python para ler Qr code a partir de uma imagem.


![](https://raw.githubusercontent.com/mxtqn/QReader/main/python.png)
#### Bibliotecas

Somente com o uso de OpenCV

```
import cv2
```

#### Funcionamento

```
import cv2
filename = "caixacompleta.jpg"                                          # Nome do arquivo que contem o Qr Code
image = cv2.imread(filename)                                            # Ler a imagem
detector = cv2.QRCodeDetector()                                         # Inicializar o detector da biblioteca
data, vertices_array, binary_qrcode = detector.detectAndDecode(image)   # Detectar e decodificar
if vertices_array is not None:                                          # Se encontrar o Qr printa o URL
    print("Conteúdo QRCode:")
    print(data)
else:
    print("Erro")
``` 
###### [leitura](https://github.com/mxtqn/qr_code/blob/main/leitura)
###### Detalhes 
```
filename = "{}" 
```
{ } deve ser preenchido como nome do arquivo dentro do projeto



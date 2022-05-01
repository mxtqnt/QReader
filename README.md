# QReader
![](https://github.com/mxtqn/QReader/blob/main/Fotos/codesqr-1024x384.jpg?raw=true)

![](https://raw.githubusercontent.com/mxtqn/QReader/efc87c037590ea691eb01fb6387c4e49a8bcbda8/Readme/python.svg) Código em Python para ler Qr code a partir de uma imagem.

#### Bibliotecas

![](https://user-images.githubusercontent.com/89314731/163866128-7dd9d26f-2ca1-4a41-b1d3-4e4377d45285.png) Somente com o uso de OpenCV

```
import cv2
```

#### 🧠 Funcionamento

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
###### Detalhes 
```
filename = "{}" 
```
{ } deve ser preenchido como nome do arquivo dentro do projeto



import cv2

# Inicializar el objeto VideoCapture para capturar video desde la cámara
cap = cv2.VideoCapture(0)

# Ciclo para mostrar cada frame del video
while True:
    # Leer un frame del video
    ret, frame = cap.read()

    # Mostrar el frame en una ventana llamada "Video"
    cv2.imshow('Video', frame)

    # Esperar 1ms antes de mostrar el siguiente frame
    # Si se presiona la tecla "q", salir del ciclo
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar el objeto VideoCapture y cerrar todas las ventanas abiertas
cap.release()
cv2.destroyAllWindows()

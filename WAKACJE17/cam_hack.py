import cv2

camera_port = 0     # numer magistrali kamerki
adj_frames = 30     # ile próbnych fotek by ustawił parametry

camera = cv2.VideoCapture(camera_port)


def get_image():            # funkcja przechwytująca obraz
    s, im = camera.read()       # musi być tupla z jakiegoś powodu
    return im

for i in range(adj_frames):     # wykonywanie fotek próbnych
    temp = get_image()
print('Taking image - smile!')
cam_capture = get_image()       # wykonanie właściwej fotki
del(camera)         # usunięcie obiektu, kamerka może być na raz przypisana tylko do jednego obiektu
file_path = "C:\pliki_py\image_test.jpg"

cv2.namedWindow('test', cv2.WINDOW_AUTOSIZE)        #tworzy okno, można zmienić rozmiar
cv2.imshow('test', cam_capture)       #pokazuje obraz/tworzy okno jeśli go nie ma
k = cv2.waitKey(0) & 0xFF    #czeka za klawiszem by zamknąć
if k == 27:     #27 to kod klwaisza ESC
    cv2.destroyAllWindows()     #zamyka wszystkie okna
elif k == ord('s'):     #ord('s') zwraca kod klawisza 's'
    cv2.imwrite(file_path, cam_capture)      #zapisuje obraz
    cv2.destroyWindow('test')     #zamyka wybrane okna

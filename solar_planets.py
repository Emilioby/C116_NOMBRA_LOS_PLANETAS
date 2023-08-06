import cv2

# Lee la imagen
img = cv2.imread("solar-system.jpg")

# Agrega texto para cada planeta
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.5
font_scale_sol = 1
font_thickness = 1
font_thickness_sol = 2
text_color = (255, 255, 255)  # Color blanco
text_color_sol=(255,0,0) # color rojo


# Agregar el texto para cada planeta
cv2.putText(img, "Sol",(50,30) , font, font_scale_sol, text_color_sol, font_thickness_sol)
cv2.putText(img, "Mercurio",(115,180) , font, font_scale, text_color, font_thickness)
cv2.putText(img, "Venus",(195,260) , font, font_scale, text_color, font_thickness)
cv2.putText(img, "Tierra",(290,165) , font, font_scale, text_color, font_thickness)
cv2.putText(img, "Marte",(380,260) , font, font_scale, text_color, font_thickness)
cv2.putText(img, "Jupiter",(560,40) , font, font_scale, text_color, font_thickness)
cv2.putText(img, "Saturno",(780,320) , font, font_scale, text_color, font_thickness)
cv2.putText(img, "Urano",(970,125) , font, font_scale, text_color, font_thickness)
cv2.putText(img, "Neptuno",(1110,300) , font, font_scale, text_color, font_thickness)

# Mostrar la imagen con el texto
cv2.imshow("Output", img)
cv2.waitKey(0)

# Guardar la imagen con el texto
cv2.imwrite("Solar_systemwithname.jpg", img)
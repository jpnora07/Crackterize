from PyQt5 import QtWidgets, QtGui, QtCore

app = QtWidgets.QApplication([])
window = QtWidgets.QWidget()
layout = QtWidgets.QVBoxLayout(window)
label = QtWidgets.QLabel("Text with Neumorphism box shadow")

# Create a first shadow effect for the inner shadow
inner_shadow = QtWidgets.QGraphicsDropShadowEffect()
inner_shadow.setBlurRadius(10)
inner_shadow.setColor(QtGui.QColor(255, 255, 255, 100))
inner_shadow.setOffset(QtCore.QPointF(2, 2))

# Create a second shadow effect for the outer shadow
outer_shadow = QtWidgets.QGraphicsDropShadowEffect()
outer_shadow.setBlurRadius(10)
outer_shadow.setColor(QtGui.QColor(0, 0, 0, 100))
outer_shadow.setOffset(QtCore.QPointF(-2, -2))

# Set both shadow effects on the label widget
label.setGraphicsEffect(inner_shadow)
label.setGraphicsEffect(outer_shadow)

layout.addWidget(label)

window.show()
app.exec_()

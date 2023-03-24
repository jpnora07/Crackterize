import sys
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QLabel, QGraphicsItem
from PyQt5.QtGui import QPixmap, QPainter, QPen, QBrush
from PyQt5.QtCore import Qt, QPoint, QRectF


class ResizableRectItem(QGraphicsRectItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setCursor(Qt.SizeAllCursor)
        self.edge_size = 10

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.orig_rect = self.rect()
        self.start_pos = event.pos()

        if event.modifiers() == Qt.ShiftModifier:
            self.corner_drag = True
            self.setCursor(Qt.SizeFDiagCursor)
        else:
            self.corner_drag = False

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)

        if self.corner_drag:
            new_pos = event.pos()
            self.setRect(QRectF(self.orig_rect.topLeft(), new_pos).normalized())
        else:
            delta = event.pos() - self.start_pos
            new_rect = self.orig_rect.translated(delta)
            self.setRect(new_rect)

        self.update(self.rect())

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self.corner_drag = False
        self.setCursor(Qt.SizeAllCursor)


class ImageCropper(QGraphicsView):
    def __init__(self, pixmap):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.pixmap = pixmap
        self.image_item = self.scene.addPixmap(self.pixmap)

        self.rectangle_item = ResizableRectItem(0, 0, pixmap.width(), pixmap.height())
        self.rectangle_item.setBrush(QBrush(Qt.red))
        self.scene.addItem(self.rectangle_item)

    def mousePressEvent(self, event):
        item = self.scene.itemAt(event.pos(), self.transform())
        if isinstance(item, ResizableRectItem):
            event.ignore()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        item = self.scene.itemAt(event.pos(), self.transform())

        if isinstance(item, ResizableRectItem):
            item.setCursor(Qt.SizeAllCursor)
            print(item.width(), item.height())
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pixmap = QPixmap("../images/10cm.jpg")
    cropper = ImageCropper(pixmap)
    cropper.show()
    sys.exit(app.exec_())

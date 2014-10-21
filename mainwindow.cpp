#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QFileDialog>
#include <QLabel>
#include <QMessageBox>
#include <QPixmap>
#include <QPainter>
#include <QResizeEvent>
#include <QWheelEvent>
#include <QMouseEvent>
#include <QDebug>

MainWindow::MainWindow(QWidget *parent, Qt::WindowFlags flags)
    : QMainWindow(parent, flags)
    , ui(new Ui_MainWindow)
    , imageScrollArea(new ImageScrollArea)
{
    // setup ui
    ui->setupUi(this);
    ui->imageGroupBoxLayout->addWidget(imageScrollArea);
    imageScrollArea->setBrushWidth(ui->brushSizeSpinBox->value());
    imageScrollArea->setBrushValue(ui->brushValueSpinBox->value());

    // signals and slots
    connect(ui->openAction, SIGNAL(triggered()),
            this, SLOT(slotOpen()));
    connect(ui->brushSizeSpinBox, SIGNAL(valueChanged(int)),
            imageScrollArea, SLOT(setBrushWidth(int)));
    connect(ui->brushValueSpinBox, SIGNAL(valueChanged(int)),
            imageScrollArea, SLOT(setBrushValue(int)));
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::slotOpen()
{
    QString filename;

    filename = QFileDialog::getOpenFileName(this, tr("Open File"), ".",
            tr("Images (*.png *.jpg *.jpeg *.bmp *.pbm *.pgm *.ppm *.xbm *.xpm)"));
    if (!filename.isEmpty()) {
        imageScrollArea->open(filename);
    }
}

ImageScrollArea::ImageScrollArea(QWidget *parent)
    : QScrollArea(parent)
    , imageLabel(new QLabel)
    , m_scaleToViewport(true)
    , m_scale(1.0f)
    , m_brushWidth(1)
    , m_brushValue(255)
    , m_brushColor(Qt::red)
{
    this->setWidget(imageLabel);
    this->setAlignment(Qt::AlignHCenter | Qt::AlignVCenter);
    imageLabel->installEventFilter(this);
    updateStatusBar();
}

ImageScrollArea::~ImageScrollArea()
{

}

void ImageScrollArea::open(const QString &filename)
{
    QImage image(filename);

    if (image.isNull()) {
        QMessageBox::critical(this, tr("Error"),
                tr("Open image file error: %1").arg(filename));
    } else {
        m_filename = filename;
        m_originImage = image;
        m_outputImage = QImage(image.width(), image.height(), QImage::Format_ARGB32);
        scaleImageToSize(this->viewport()->size());
    }
}

bool ImageScrollArea::eventFilter(QObject *watched, QEvent *event)
{
    if (watched == imageLabel) {
        switch (event->type()) {
        case QEvent::MouseMove:
            {
                QMouseEvent *mouseEvent = static_cast<QMouseEvent *>(event);
                if (mouseEvent->buttons() & Qt::LeftButton) {
                    QRect rect(mouseEvent->x() - m_brushWidth, mouseEvent->y() - m_brushWidth,
                               m_brushWidth * 2, m_brushWidth * 2);
                    fillScaledImage(rect);
                    imageLabel->update(rect);
                }
            }
            break;
        case QEvent::Paint:
            {
                QPaintEvent *paintEvent = static_cast<QPaintEvent *>(event);
                QRect rect = paintEvent->rect();
                QPoint *points = new QPoint[rect.width() * rect.height()];
                int pointNum = 0;
                int x1, y1, x2, y2;
                QPainter painter;

                if (m_outputImage.isNull()) {
                    return false;
                }

                // points
                x1 = std::max(0, rect.left());
                y1 = std::max(0, rect.top());
                x2 = rect.right();
                y2 = rect.bottom();
                for (int y = y1; y <= y2; ++y) {
                    quint32 *line = reinterpret_cast<quint32 *>(m_outputImage.scanLine(int(y / m_scale)));
                    for (int x = x1; x <= x2; ++x) {
                        if (line[int(x / m_scale)]) {
                            points[pointNum].setX(x);
                            points[pointNum].setY(y);
                            ++pointNum;
                        }
                    }
                }

                // draw
                painter.begin(imageLabel);
                painter.drawImage(rect, m_scaledImage, rect);
                painter.setPen(m_brushColor);
                painter.drawPoints(points, pointNum);
                painter.end();

                delete []points;
            }
            return true;
            break;

        default:
            break;
        }
    }
    return QScrollArea::eventFilter(watched, event);
}

bool ImageScrollArea::viewportEvent(QEvent *event)
{
    switch (event->type()) {
    case QEvent::Resize:
        {
        QResizeEvent *resizeEvent = static_cast<QResizeEvent *>(event);
        if (m_scaleToViewport && !m_originImage.isNull()) {
            scaleImageToSize(resizeEvent->size());
        }
        }
        break;
    case QEvent::Wheel:
        {
        QWheelEvent *wheelEvent = static_cast<QWheelEvent *>(event);
        if (wheelEvent->modifiers() == Qt::ControlModifier) {
            QPoint numPixels = wheelEvent->pixelDelta();
            QPoint numDegrees = wheelEvent->angleDelta() / 8;

            if (!numPixels.isNull()) {
                zoom(numPixels.y() / 30); // not sure for this
            } else if (!numDegrees.isNull()) {
                zoom(numDegrees.y() / 15);
            }
        }
        }
        break;
    }
    return QScrollArea::viewportEvent(event);
}

void ImageScrollArea::zoom(int step)
{
    float scale = m_scale;

    scale += step * 0.1f;
    if (scale > 0) {
        m_scaleToViewport = false;
        scaleImage(scale);
    }
}

void ImageScrollArea::scaleImage(float scale)
{
    m_scale = scale;
    m_scaledImage = m_originImage.scaled(m_scale * m_originImage.width(),
                                         m_scale * m_originImage.height());
    imageLabel->setPixmap(QPixmap::fromImage(m_scaledImage));
    imageLabel->resize(imageLabel->sizeHint());
    updateStatusBar();
}

void ImageScrollArea::scaleImageToSize(const QSize &size)
{
    float scale;

    scale = std::min(size.width() / float(m_originImage.width()),
                     size.height() / float(m_originImage.height()));
    if (scale > 1.0) {
        scale = 1.0;
    }
    scaleImage(scale);
}

void ImageScrollArea::fillScaledImage(const QRect &rect)
{
    int x1, y1, x2, y2;

    x1 = std::max(0, int(rect.left() / m_scale));
    y1 = std::max(0, int(rect.top() / m_scale));
    x2 = int(rect.right() / m_scale);
    y2 = int(rect.bottom() / m_scale);

    for (int y = y1; y <= y2; ++y) {
        quint32 *line = reinterpret_cast<quint32 *>(m_outputImage.scanLine(y));
        for (int x = x1; x <= x2; ++x) {
            line[x] = m_brushValue;
        }
    }
}

void ImageScrollArea::updateStatusBar()
{
    QString message;
    QMainWindow *win;

    if (m_originImage.isNull()) {
        message = tr("No image");
    } else {
        message = tr("Origin image size: (%1, %2), scale: %3)")
            .arg(m_originImage.width()).arg(m_originImage.height()).arg(m_scale);
    }
    win = dynamic_cast<QMainWindow *>(this->window());
    if (win) {
        win->statusBar()->showMessage(message);
    }
}

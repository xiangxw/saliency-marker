#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QScrollArea>
#include <QImage>
#include <QColor>

class Ui_MainWindow;
class ImageScrollArea;
class QLabel;

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = 0, Qt::WindowFlags flags = 0);
    ~MainWindow();

private slots:
    void slotOpen();

private:
    Ui_MainWindow *ui;
    ImageScrollArea *imageScrollArea;
};

class ImageScrollArea : public QScrollArea
{
    Q_OBJECT

public:
    ImageScrollArea(QWidget *parent = 0);
    ~ImageScrollArea();

public slots:
    void setBrushWidth(int width) {m_brushWidth = width;}
    void setBrushValue(int value) {m_brushValue = value;}
    void open(const QString &filename);

protected:
    bool eventFilter(QObject *watched, QEvent *event);
    bool viewportEvent(QEvent *event);

private:
    void zoom(int step);
    void scaleImage(float scale);
    void scaleImageToSize(const QSize &size);
    void fillScaledImage(const QRect &rect);
    void updateStatusBar();

    QLabel *imageLabel;
    bool m_scaleToViewport;
    float m_scale;
    QString m_filename;
    QImage m_originImage;
    QImage m_outputImage;
    QImage m_scaledImage;
    int m_brushWidth;
    int m_brushValue;
    QColor m_brushColor;
};

#endif // end MAINWINDOW_H

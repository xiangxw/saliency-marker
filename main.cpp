#include "mainwindow.h"
#include <QApplication>
#include <QIcon>

int main(int argc, char **argv)
{
    QApplication app(argc, argv);
    MainWindow win;

    app.setWindowIcon(QIcon(":images/saliency-marker.svg"));
    win.show();
    return app.exec();
}

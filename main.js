const { app, BrowserWindow } = require('electron')

let mainWindow

app.on('ready', () => {

    mainWindow = new BrowserWindow({
        width: 500,
        height: 500,
        resizable: false,
        autoHideMenuBar: true,
        icon: __dirname + 'assets/img/icon.ico'
    })

    mainWindow.loadURL(`file://${__dirname}/index.html`)

})
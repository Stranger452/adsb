const electron = require('electron')
const { app, BrowserWindow, ipcMain } = electron;

const { spawn } = require('child_process');

 

let mainWindow;

 

app.on('ready', () => {

  mainWindow = new BrowserWindow({

    width: 800,

    height: 600,

    webPreferences: {

      nodeIntegration: true,

    },

  });

 

  mainWindow.loadFile('index.html');

});

 

ipcMain.on('run-python-code', (event) => {

  const pythonProcess = spawn('python', ['/home/irtaza/Downloads/ADSB-Out-master/main.py']);

 

  pythonProcess.stdout.on('data', (data) => {

    // Send Python output to the renderer process

    mainWindow.webContents.send('python-output', data.toString());

  });

 

  pythonProcess.stderr.on('data', (data) => {

    // Handle Python errors, if any

    console.error('Python Error:', data.toString());

  });

 

  pythonProcess.on('close', (code) => {

    console.log(`Python process exited with code ${code}`);

  });

});
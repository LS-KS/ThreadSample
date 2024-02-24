import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

import io.qt.textproperties 1.0

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    Controller{
        id: controller
    }
    
    RowLayout{
        anchors.fill: parent
        Layout.fillHeight: true
        Layout.fillWidth: true
        spacing: 15
        ColumnLayout{
            id: buttonColumn
            Layout.fillHeight: true
            Layout.fillWidth: true
            Button{
                id: btnMessage1
                text: "Message1"
                onClicked: msgLabel.text = "Message 1..."
            }
            Button{
                id: btnMessage2
                text: "Message2"
                onClicked: msgLabel.text = "Message 2 ..."
            }
            Button{
                id: btnRun
                text: "Run fibonacci"
                onClicked: controller.start()
            }
            Button{
                id: btnInt
                text: "Interrupt"
                enabled: false
                onClicked: {
                    btnReset.enabled = false
                    controller.stop()
                }
            }
            Button{
                id: btnReset
                text: "Reset Threadloop"
                enabled: false
                onClicked: controller.resetThreadloop()
            }

            Label{
                id: msgLabel
                text: ""
            }
            
        }
        ColumnLayout{
            id: resultLayout
            Layout.fillHeight: true
            Layout.fillWidth: true
            TextArea{
                id: resultArea
                Layout.fillHeight: true
                Layout.fillWidth: true
                text: ""
            }
            ProgressBar{
                id: pBar
                Layout.fillWidth:  true
                value: 0
                from: 0
                to: 25
            }

            TextArea{
               id: explaination
               readOnly: true
               Layout.fillWidth: true
               wrapMode: "WordWrap"
               text: "Use 'Message 1' and 'Message 2' to test if thread is deadlocked or not."+
                     "Use 'Run fibonacci' to start long running computation. Use 'Interrupt' to interrupt long running computation."
            }
        }
    }
    Connections{
        target: controller
        function onResult(result){
            resultArea.text ="neues Ergebnis: "+ result +"\n"  + resultArea.text
        }
        function onProgress(p){
            pBar.value = p
        }
        function onStarted(){
            btnRun.enabled = false
            btnInt.enabled = true
            btnReset.enabled = true
        }
        function onFinished(){
            btnRun.enabled = true
            btnInt.enabled = false
            btnReset.enabled = false
            resultArea.text ="Thread beendet.\n"  + resultArea.text
        }
    }
}

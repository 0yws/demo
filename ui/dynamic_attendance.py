# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dynamic_attendance.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DynamicAttendance(object):
    def setupUi(self, DynamicAttendance):
        DynamicAttendance.setObjectName("DynamicAttendance")
        DynamicAttendance.resize(1111, 771)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(DynamicAttendance)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(DynamicAttendance)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.video_source_txt = QtWidgets.QLineEdit(DynamicAttendance)
        self.video_source_txt.setObjectName("video_source_txt")
        self.horizontalLayout_8.addWidget(self.video_source_txt)
        self.open_source_btn = QtWidgets.QPushButton(DynamicAttendance)
        self.open_source_btn.setObjectName("open_source_btn")
        self.horizontalLayout_8.addWidget(self.open_source_btn)
        self.close_source_btn = QtWidgets.QPushButton(DynamicAttendance)
        self.close_source_btn.setObjectName("close_source_btn")
        self.horizontalLayout_8.addWidget(self.close_source_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.line_7 = QtWidgets.QFrame(DynamicAttendance)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_7.addWidget(self.line_7)
        self.label_11 = QtWidgets.QLabel(DynamicAttendance)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.video_resource_list = QtWidgets.QListWidget(DynamicAttendance)
        self.video_resource_list.setObjectName("video_resource_list")
        self.verticalLayout_7.addWidget(self.video_resource_list)
        self.line_8 = QtWidgets.QFrame(DynamicAttendance)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_7.addWidget(self.line_8)
        self.label_12 = QtWidgets.QLabel(DynamicAttendance)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_7.addWidget(self.label_12)
        self.video_resource_file_list = QtWidgets.QListWidget(DynamicAttendance)
        self.video_resource_file_list.setObjectName("video_resource_file_list")
        self.verticalLayout_7.addWidget(self.video_resource_file_list)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_13 = QtWidgets.QLabel(DynamicAttendance)
        self.label_13.setStyleSheet("font: 12pt \"华文琥珀\";")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_10.addWidget(self.label_13)
        self.show_anno_ckb = QtWidgets.QCheckBox(DynamicAttendance)
        self.show_anno_ckb.setChecked(True)
        self.show_anno_ckb.setObjectName("show_anno_ckb")
        self.horizontalLayout_10.addWidget(self.show_anno_ckb)
        self.show_raw_lbl_ckb = QtWidgets.QCheckBox(DynamicAttendance)
        self.show_raw_lbl_ckb.setObjectName("show_raw_lbl_ckb")
        self.horizontalLayout_10.addWidget(self.show_raw_lbl_ckb)
        self.auto_close_ahead_ckb = QtWidgets.QCheckBox(DynamicAttendance)
        self.auto_close_ahead_ckb.setObjectName("auto_close_ahead_ckb")
        self.horizontalLayout_10.addWidget(self.auto_close_ahead_ckb)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.verticalLayout_9.addLayout(self.horizontalLayout_10)
        self.video_screen = QtWidgets.QLabel(DynamicAttendance)
        self.video_screen.setAutoFillBackground(False)
        self.video_screen.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.video_screen.setFrameShadow(QtWidgets.QFrame.Plain)
        self.video_screen.setText("")
        self.video_screen.setObjectName("video_screen")
        self.verticalLayout_9.addWidget(self.video_screen)
        self.video_process_bar = QtWidgets.QSlider(DynamicAttendance)
        self.video_process_bar.setAutoFillBackground(False)
        self.video_process_bar.setStyleSheet(" QSlider {\n"
"    background-color: rgba(22, 22, 22, 0.7);\n"
"    border-radius: 5px;\n"
"}\n"
" \n"
"QSlider::sub-page:horizontal {\n"
"    background-color: #FF7826;\n"
"    height:4px;\n"
"    border-radius: 2px;\n"
"}\n"
" \n"
"QSlider::add-page:horizontal {\n"
"    background-color: #7A7B79;\n"
"    height:4px;\n"
"    border-radius: 2px;\n"
"}\n"
" \n"
"QSlider::groove:horizontal {\n"
"    background:transparent;\n"
"    height:10px;\n"
"}\n"
" \n"
"QSlider::handle:horizontal {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px -2px 0px -2px;\n"
"    border-radius: 5px;\n"
"    background: white;\n"
"}")
        self.video_process_bar.setMinimum(-1)
        self.video_process_bar.setMaximum(-1)
        self.video_process_bar.setProperty("value", -1)
        self.video_process_bar.setOrientation(QtCore.Qt.Horizontal)
        self.video_process_bar.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.video_process_bar.setTickInterval(0)
        self.video_process_bar.setObjectName("video_process_bar")
        self.verticalLayout_9.addWidget(self.video_process_bar)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.time_process_label = QtWidgets.QLabel(DynamicAttendance)
        self.time_process_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.time_process_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.time_process_label.setObjectName("time_process_label")
        self.horizontalLayout_11.addWidget(self.time_process_label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem2)
        self.play_video_btn = QtWidgets.QPushButton(DynamicAttendance)
        self.play_video_btn.setObjectName("play_video_btn")
        self.horizontalLayout_11.addWidget(self.play_video_btn)
        self.stop_playing_btn = QtWidgets.QPushButton(DynamicAttendance)
        self.stop_playing_btn.setObjectName("stop_playing_btn")
        self.horizontalLayout_11.addWidget(self.stop_playing_btn)
        self.early_stop_video_btn = QtWidgets.QPushButton(DynamicAttendance)
        self.early_stop_video_btn.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.early_stop_video_btn.setObjectName("early_stop_video_btn")
        self.horizontalLayout_11.addWidget(self.early_stop_video_btn)
        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 3)
        self.horizontalLayout_11.setStretch(2, 1)
        self.horizontalLayout_11.setStretch(3, 1)
        self.verticalLayout_9.addLayout(self.horizontalLayout_11)
        self.verticalLayout_9.setStretch(1, 8)
        self.verticalLayout_9.setStretch(3, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_9)
        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_14 = QtWidgets.QLabel(DynamicAttendance)
        self.label_14.setStyleSheet("font: 12pt \"华文琥珀\";")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_3.addWidget(self.label_14)
        self.refresh_face_bank_btn = QtWidgets.QPushButton(DynamicAttendance)
        self.refresh_face_bank_btn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.refresh_face_bank_btn.setText("")
        self.refresh_face_bank_btn.setObjectName("refresh_face_bank_btn")
        self.horizontalLayout_3.addWidget(self.refresh_face_bank_btn)
        self.face_bank_list_cbx = QtWidgets.QComboBox(DynamicAttendance)
        self.face_bank_list_cbx.setObjectName("face_bank_list_cbx")
        self.horizontalLayout_3.addWidget(self.face_bank_list_cbx)
        self.class_list_filter_txt = QtWidgets.QLineEdit(DynamicAttendance)
        self.class_list_filter_txt.setObjectName("class_list_filter_txt")
        self.horizontalLayout_3.addWidget(self.class_list_filter_txt)
        self.student_list_filter_txt = QtWidgets.QLineEdit(DynamicAttendance)
        self.student_list_filter_txt.setObjectName("student_list_filter_txt")
        self.horizontalLayout_3.addWidget(self.student_list_filter_txt)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_3.setStretch(5, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.student_list = QtWidgets.QListWidget(DynamicAttendance)
        self.student_list.setFlow(QtWidgets.QListView.LeftToRight)
        self.student_list.setProperty("isWrapping", True)
        self.student_list.setWordWrap(True)
        self.student_list.setObjectName("student_list")
        self.verticalLayout_5.addWidget(self.student_list)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.line = QtWidgets.QFrame(DynamicAttendance)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_5.addWidget(self.line)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_21 = QtWidgets.QLabel(DynamicAttendance)
        self.label_21.setStyleSheet("font: 12pt \"华文琥珀\";")
        self.label_21.setObjectName("label_21")
        self.verticalLayout.addWidget(self.label_21)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_19 = QtWidgets.QLabel(DynamicAttendance)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout.addWidget(self.label_19)
        self.face_match_threshold_dspin = QtWidgets.QDoubleSpinBox(DynamicAttendance)
        self.face_match_threshold_dspin.setMaximum(100.0)
        self.face_match_threshold_dspin.setSingleStep(1.0)
        self.face_match_threshold_dspin.setProperty("value", 70.0)
        self.face_match_threshold_dspin.setObjectName("face_match_threshold_dspin")
        self.horizontalLayout.addWidget(self.face_match_threshold_dspin)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_20 = QtWidgets.QLabel(DynamicAttendance)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_2.addWidget(self.label_20)
        self.front_face_err_dspin = QtWidgets.QDoubleSpinBox(DynamicAttendance)
        self.front_face_err_dspin.setEnabled(False)
        self.front_face_err_dspin.setObjectName("front_face_err_dspin")
        self.horizontalLayout_2.addWidget(self.front_face_err_dspin)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line_2 = QtWidgets.QFrame(DynamicAttendance)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_18 = QtWidgets.QLabel(DynamicAttendance)
        self.label_18.setStyleSheet("font: 12pt \"华文琥珀\";")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_6.addWidget(self.label_18)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.student_num_lbl = QtWidgets.QLabel(DynamicAttendance)
        self.student_num_lbl.setObjectName("student_num_lbl")
        self.horizontalLayout_6.addWidget(self.student_num_lbl)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.attended_list = QtWidgets.QListWidget(DynamicAttendance)
        self.attended_list.setObjectName("attended_list")
        self.verticalLayout_2.addWidget(self.attended_list)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_17 = QtWidgets.QLabel(DynamicAttendance)
        self.label_17.setStyleSheet("font: 12pt \"华文琥珀\";")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_3.addWidget(self.label_17)
        self.absented_list = QtWidgets.QListWidget(DynamicAttendance)
        self.absented_list.setObjectName("absented_list")
        self.verticalLayout_3.addWidget(self.absented_list)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_5.setStretch(0, 7)
        self.horizontalLayout_5.setStretch(2, 4)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.retranslateUi(DynamicAttendance)
        QtCore.QMetaObject.connectSlotsByName(DynamicAttendance)

    def retranslateUi(self, DynamicAttendance):
        _translate = QtCore.QCoreApplication.translate
        DynamicAttendance.setWindowTitle(_translate("DynamicAttendance", "动态点名"))
        self.label_10.setText(_translate("DynamicAttendance", "视频源"))
        self.video_source_txt.setText(_translate("DynamicAttendance", "resource/videos/front_cheat.mp4"))
        self.open_source_btn.setText(_translate("DynamicAttendance", "开启源"))
        self.close_source_btn.setText(_translate("DynamicAttendance", "关闭源"))
        self.label_11.setText(_translate("DynamicAttendance", "视频通道"))
        self.label_12.setText(_translate("DynamicAttendance", "本地视频"))
        self.label_13.setText(_translate("DynamicAttendance", "动态点名"))
        self.show_anno_ckb.setText(_translate("DynamicAttendance", "显示标注"))
        self.show_raw_lbl_ckb.setText(_translate("DynamicAttendance", "显示原始检测"))
        self.auto_close_ahead_ckb.setText(_translate("DynamicAttendance", "自动提前截止"))
        self.time_process_label.setText(_translate("DynamicAttendance", "00:00:00/00:00:00"))
        self.play_video_btn.setText(_translate("DynamicAttendance", "播放"))
        self.stop_playing_btn.setText(_translate("DynamicAttendance", "暂停"))
        self.early_stop_video_btn.setText(_translate("DynamicAttendance", "提前截止"))
        self.label_14.setText(_translate("DynamicAttendance", "学生列表"))
        self.class_list_filter_txt.setPlaceholderText(_translate("DynamicAttendance", "班级过滤条件"))
        self.student_list_filter_txt.setPlaceholderText(_translate("DynamicAttendance", "班级过滤条件"))
        self.label_21.setText(_translate("DynamicAttendance", "签到选项"))
        self.label_19.setText(_translate("DynamicAttendance", "人脸匹配阈值"))
        self.label_20.setText(_translate("DynamicAttendance", "正脸误差(取消)"))
        self.label_18.setText(_translate("DynamicAttendance", "已签到"))
        self.student_num_lbl.setText(_translate("DynamicAttendance", "人数：0/0"))
        self.label_17.setText(_translate("DynamicAttendance", "未签到"))
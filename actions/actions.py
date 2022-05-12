# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# This is a simple example for a custom action which utters "Hello World!"

import sqlite3
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher

sqliteConnection = sqlite3.connect(R'C:\Users\lehoangvu24\Desktop\Rasa\Chatbot\GV_HTTTQL.db')
cursor = sqliteConnection.cursor()
print("Kết nối thành công")

# Truy vấn sqlite lấy thông tin giảng viên
class ActionAskKnowledgeBaseLoaiSanPham(Action):
    def name(self):
        return "action_custom_Giang_vien"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = tracker.latest_message['text']
        text_input = text
        thong_tin = next(tracker.get_latest_entity_values("giang vien"), None)
		# thong_tin_ep = str(thong_tin)
		# des_tt = tracker.get_latest_entity_values("giang vien")

        sqlite_select_Query = f'''SELECT * from GV where Hoten like "%{thong_tin}%"'''
        
        cursor.execute(sqlite_select_Query)
        record = cursor.fetchall()
        # check = False
        # print(text_input)
        s = "0"
        for result in record:

            Hoten = result[0]
            Email = result[1]
            Chucvu = result[2]
            SĐt = s + str(result[3])
    
        dispatcher.utter_message(f"Đây là thông tin bạn cần về giảng viên {Hoten} nhé: \n Email: {Email} \n Chức vụ: {Chucvu} \n Số điện thoại: {SĐt}")
        return []

class ActionAskKnowledgeBaseThongtin(Action):
    def name(self):
        return "action_custom_thong_tin"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = tracker.latest_message['text']
        text_input = text
        thong_tin_ct = next(tracker.get_latest_entity_values("thong_tin"), None)
        thong_tin_cts = str(thong_tin_ct).title()
     
        if(thong_tin_ct != None):
        
            sqlite_select_Query = f'''SELECT * from Thongtin where Tên like "%{thong_tin_cts}%"'''
        
            cursor.execute(sqlite_select_Query)
            Ketqua = cursor.fetchall()
           
            for result in Ketqua:

                ten = result[0]
                Diachi = result[1]
                SĐT = str(result[2])
           
            dispatcher.utter_message(
                f"Đây là thông tin của {ten} bạn nhé: \n Địa chỉ: {Diachi} \n Số điện thoại: {SĐT}")

        
        else:
            dispatcher.utter_message(
                f"Thông tin bạn cung cấp hiện tại mình không có câu trả lời. Rất xin lỗi, mời bạn đổi câu hỏi khác!!")


        return []
# class ActionDefaultFallback(Action):
#     """Executes the fallback action and goes back to the previous state
#     of the dialogue"""

#     def name(self) -> Text:
#         return ACTION_DEFAULT_FALLBACK_NAME

#     async def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="my_custom_fallback_template")

#         # Revert user message which led to fallback.
#         return [UserUtteranceReverted()]
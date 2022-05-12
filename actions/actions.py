# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
# #
# from rasa_sdk import Action, Tracker
# from rasa_sdk.events import SlotSet,  EventType
# from rasa_sdk.executor import CollectingDispatcher

# from smtplib import SMTP
# import requests
# import json, os

# def name_cap(text):
#     tarr = text.split()
#     for idx in range(len(tarr)):
#         tarr[idx] = tarr[idx].capitalize()
#     return ' '.join(tarr)

# class action_save_cust_info(Action):
#     def name(self):
#         return 'action_save_cust_info'

#     def run(self, dispatcher, tracker, domain):
#         user_id = (tracker.current_state())["sender_id"]
#         print(user_id)
#         cust_name = next(tracker.get_latest_entity_values("cust_name"), None)
#         cust_sex = next(tracker.get_latest_entity_values("cust_sex"), None)
#         bot_position = "Mình"

#         if (cust_sex is  None):
#             cust_sex = "Bạn"

#         if (cust_sex == "anh") | (cust_sex == "chị"):
#            bot_position = "em"
#         elif (cust_sex == "cô") | (cust_sex == "chú"):
#             bot_position = "cháu"
#         else:
#             cust_sex = "Bạn"
#             bot_position = "Mình"

#         if not cust_name:
#             dispatcher.utter_template("utter_greet_with_name",tracker)
#             return []

#         print (name_cap(cust_name))
#         return [SlotSet('cust_name', " "+name_cap(cust_name)),SlotSet('cust_sex', name_cap(cust_sex)),SlotSet('bot_position', name_cap(bot_position))]

# class action_reset_slot(Action):

#     def name(self):
#         return "action_reset_slot"

#     def run(self, dispatcher, tracker, domain):
#         return [SlotSet("transfer_nick", None),SlotSet("transfer_amount", None),SlotSet("transfer_amount_unit", None)]

			# class GetName(Action):
			# 	def name(self):
			# 		return 'action_name'
					
			# 	def run(
			# 		self,
			# 		dispatcher: CollectingDispatcher,
			# 		tracker: Tracker,
			# 		domain: Dict[Text, Any],
					
			# 	)-> List[EventType]:
			# 		import requests
			# 		# fb_access_token = ("EAAGYniiVkQMBACTLOlx4xK76k7UcoITqVbjIODjhZAa10lE0ul7Q4nW8EAhwFA5UCoCLRpyksRZB3Rroi1ln4OZB8VR11KyE2AVaC0fQgOaLDIGwBdvHX8xNvgkSsOKVavEghKcHabZACkqYB1LlmnfuRKvPZCZCRCbybzD4ZBon9bxvHir7ao845eXG7gATxkZD")
			# 		fb_access_token = ("EAALpq0lPXikBABYnERvexP3qzunbZCGLv1VWkwFleRUSHmA6A7oiKCIxn6FG9yLq6FuEdnNpEJdMMHDRdIGng4Qb2PgpIRNh54gLldeolofzZAIY8BfNzF4tMFa2zDGrD0Y8H7Y4oDLyCmZAqmqdTlQtJuszZAsezfKZAZBOxd9E6man9g7XwD")
					
			# 		most_recent_state = tracker.current_state()
			# 		sender_id = most_recent_state['sender_id']
					
			# 		r = requests.get('https://graph.facebook.com/{}?fields=first_name,middle_name,last_name&access_token={}'.format(sender_id, fb_access_token)).json()
			# 		first_name = r["first_name"]
			# 		middle_name = r["middle_name"]
			# 		last_name = r["last_name"]
					
			# 		dispatcher.utter_message("Chào {} {} {} nhé, mình có thể giúp gì được cho bạn?' ".format(last_name, middle_name, first_name))
			# 		# return [SlotSet('name', first_name), SlotSet('surname', last_name)]

# class ActionService(Action):

# 	def name(self) -> Text:
# 		return "action_service"

# 	def run(self, dispatcher: CollectingDispatcher,
# 			tracker: Tracker,
# 			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

# 		buttons = [
# 			{"payload":"/tuition", "title": "Hoc phi"},
# 			{"payload":"/education_program", "title": "Chuong trinh dao tao"}
# 		]
# 		dispatcher.utter_message(text="Ban muon hoi ve van de gi?", buttons=buttons)

# 		return []
import sqlite3
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher

<<<<<<< HEAD
sqliteConnection = sqlite3.connect(R'C:\Users\lehoangvu24\Desktop\Rasa\Chatbot\db_GV_Mis.db')
=======
sqliteConnection = sqlite3.connect(R'C:\Users\LENOVO\rasa_des_ver2\RASA_FINAL\Chatbot\GV_HTTTQL.db')
>>>>>>> 0c24e6e9174601274db556237e3258f30eb7879e
cursor = sqliteConnection.cursor()
# print("Kết nối thành công")

# Truy vấn sqlite lấy thông tin giảng viên
class ActionAskKnowledgeBaseGiangVien(Action):
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

        sqlite_select_Query = f'''SELECT * from GVs where Hoten like "%{thong_tin}%"'''
        
        cursor.execute(sqlite_select_Query)
        record = cursor.fetchall()
<<<<<<< HEAD
        result = record[-1]
        Hoten = result[0]
        Email = result[1]
        Chucvu = result[2]
        SĐT = result[3]
        dispatcher.utter_message(f"Đây là thông tin bạn cần  nhé: {Hoten}, {Email}, {Chucvu}, {SĐT}")
=======
        # check = False
        # print(text_input)
        s = "0"
        for result in record:

            Hoten = result[0]
            Email = result[1]
            Chucvu = result[2]
            SĐt = s + str(result[3])
    
        dispatcher.utter_message(f"Đây là thông tin bạn cần về giảng viên {Hoten} nhé: \n Email: {Email} \n Chức vụ: {Chucvu} \n Số điện thoại: {SĐt}")
>>>>>>> 0c24e6e9174601274db556237e3258f30eb7879e
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
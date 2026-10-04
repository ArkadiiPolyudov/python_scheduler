import json
from datetime import datetime

class Scheduler:
    def __init__(self):
        self.meetings = []
        self.load_meetings()

    def save_meetings(self):
        with open("meetings.json", "w") as file:
            json.dump(self.meetings, file)
    
    def load_meetings(self):
        try:
            with open("meetings.json", "r") as file:
                self.meetings = json.load(file)
        except FileNotFoundError:
            self.meetings = []


    def time_to_minutes(
        self,
        time: str,
    ) -> int:
        hours, minutes = time.split(":")
        return int(hours) * 60 + (int(minutes))




    def find_free_time_slots (
        self,
        start_time: str,
        end_time: str,
        slot_duration: int,
    ) -> list[str]:

    
        busy_slots = []
        for meeting in self.meetings:
            busy_slots.append(meeting['time'])
    

        all_slots = []
        for i in range(self.time_to_minutes(start_time), self.time_to_minutes(end_time), slot_duration):
            slot = f'{i // 60:02}:{i % 60:02}'
            all_slots.append(slot)

        free_slots = list(set(all_slots) - set(busy_slots))
        sorted_free_slots = sorted(free_slots)
        return sorted_free_slots



    def find_meeting (
        self, 
        title: str,
    ) -> dict | None:
        for meeting in self.meetings:
            if meeting["title"] == title:
                return meeting
        return None
    



    def add_meeting_in_meetings (
        self, 
        title: str, 
        time: str, 
        name: str,
    ) -> bool:
        if self.find_meeting(title) is not None:
            return False


            
        try:
            not_clean_time = datetime.strptime(time, "%H:%M")
        except ValueError:
            return False

        clean_time = not_clean_time.strftime("%H:%M")
        
        for meeting in self.meetings:
            if meeting["time"] == clean_time:
                return False
        
        new_meeting = {
            "title": title,
            "time": clean_time,
            "name": name,                            
            }

        self.meetings.append(new_meeting)
        self.save_meetings()
        return True

    def delete_meeting(
        self,
        title: str,
    ) -> bool:
        for meeting in self.meetings:
            if title == meeting["title"]:
                self.meetings.remove(meeting)
                self.save_meetings()
                return True
        return False


    


scheduler = Scheduler()
print(scheduler.add_meeting_in_meetings("test12","2599","test12"))
print(scheduler.meetings)
from collections import UserDict
from datetime import datetime

class Field:
    def __init__(self, value) -> None:
        self.__value = value
        self.value = value
    
    def __str__(self) -> str:
        return self.value
    
    def __repr__(self) -> str:
        return str(self)
        
    def __eq__(self, other):
        return self.value == other.value

class Name(Field):
    ...
    

class Phone(Field):
    ...
    # def __init__(self):
    #     super().__init__()

    # @property
    # def value(self):
    #     return self.__value
    
    # @value.setter
    # def value(self, value):
    #     #print(value.isdigit())
    #     #print(len(value))
    #     if (value.isdigit()) and (len(value) > 3):
    #         self.__value = value    


class Birthday(Field):
    ...


class Record:
    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None) -> None:
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
        if birthday:
            self.birthday = birthday
    
    def add_phone(self, phone: Phone = None):
        #if phone.value not in [p.value for p in self.phones]:
        if phone not in self.phones:
            self.phones.append(phone)
            return f"phone {phone} add to contact {self.name}"
        return f"{phone} present in phones of contact {self.name}"
    
    def change_phone(self, old_phone, new_phone):
        for idx, p in enumerate(self.phones):
            if old_phone.value == p.value:
                self.phones[idx] = new_phone
                return f"old phone {old_phone} change to {new_phone}"
        return f"{old_phone} not present in phones of contact {self.name}"
    
    def del_phone(self, phone: Phone = None):
        i = 0
        result = ""
        for p in self.phones:
            if phone == p:
                self.phones.pop(i)
                result = f"{phone} delete from phones of contact {self.name}"
            i += 1
        if result == "":
            result = f"contact {self.name} have not phone {phone}"
        return result
    
    def days_to_birthday(self, birthday):
        '''возвращает количество дней до следующего дня рождения'''
        date_now = datetime.now()
        days_in_year = 366 if (date_now.year+1)%4 == 0 else 365
        birthday_split = birthday.split('-')
        birthday_next = datetime(year=date_now.year+1, month=int(birthday_split[1]), day=int(birthday_split[2]))
        difference = birthday_next.date() - date_now.date()
        days_offset = difference.days
        days_offset = days_offset - days_in_year if days_offset > days_in_year else days_offset
        return days_offset

    def __str__(self) -> str:
        #return f"{self.name}: {', '.join(str(p) for p in self.phones)}"
        result = f"{self.name}: {', '.join(str(p) for p in self.phones) if self.phones else ''} {self.birthday}"
        return result
    
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[str(record.name)] = record
        return f"Contact {record} add success"

    def __str__(self) -> str:
        return "\n".join(str(r) for r in self.data.values())
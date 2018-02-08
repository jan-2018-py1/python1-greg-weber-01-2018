

class Call(object):
    def __init__(self, id, name, phone_number, time, reason):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.time = time
        self.reason = reason

    def display(self):
        print "id:", self.id
        print "name:", self.name
        print "phone number", self.phone_number 
        print "time:", self.time 
        print "reason for call:", self.reason
        return self
    
class Call_Center(object):
    def __init__(self):
        self.calls = []
        # calling self.queue will give you the current q length
        self.queue = 0

    def add(self, id, name, phone_number, time, reason ):
        call_list = Call(id, name, phone_number, time, reason)
        self.calls.append(call_list)
        self.queue +=1 
        return self

    def remove(self):
        self.calls.pop(0)
        self.queue -= 1
        return self
    
    def info(self):
        print ' '*50
        print 'Queue order by time call received:'
        q_position = 1
        for caller in range(len(self.calls)):
            print self.calls[caller].name
            print self.calls[caller].phone_number
            print 'queue position', q_position
            q_position +=1
        print '=='*10,  'queue length:', self.queue
        return self
    
    def remove_by_number(self, phone_number):
        for caller in range(len(self.calls)):
            if self.calls[caller].phone_number == phone_number:
                idx = self.calls.index(self.calls[caller])
        self.calls.pop(idx)
        self.queue -= 1
        return self


call_queue = Call_Center()

call_queue.add(1, 'Greg', '555-5555', '10:45', 'directions').add(2, 'Joe', '333-3333', '11:00',  'hrs open?').info()
call_queue.add(3, 'Kristin', '222-2222', "11:01", 'directions').info()
call_queue.remove_by_number('333-3333').info()
call_queue.remove().info()
call_queue.add(3,'Jim', '111-1111', '11:07', 'change user info').info()





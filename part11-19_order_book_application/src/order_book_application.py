class Task:
    id = 0

    def __init__(self, desc: str, name: str, hours: int):
        self.description = desc
        self.programmer = name
        self.workload = hours
        self.finished = False
        Task.id += 1
        self.id = Task.id
        

    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True

    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {'NOT FINISHED' if self.finished == False else 'FINISHED'}"

class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description, programmer, workload):
        self.orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.orders

    def programmers(self):
        return list({order.programmer for order in self.orders})

    def mark_finished(self, id: int):
        for task in self.orders:
            if task.id == id:
                task.mark_finished()
                return
        # if id not in [order.id for order in self.orders]:
        raise ValueError("id not found")

    def finished_orders(self):
        return [order for order in self.orders if order.is_finished()]

    def unfinished_orders(self):
        return [order for order in self.orders if not order.is_finished()]
    
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError("programmer not found")
        return (
            len([item for item in self.finished_orders() if item.programmer == programmer]),
            len([item for item in self.unfinished_orders() if item.programmer == programmer]),
            sum([item.workload for item in self.finished_orders() if item.programmer == programmer]),
            sum([item.workload for item in self.unfinished_orders() if item.programmer == programmer])
        )

class OrderBookApplication:
    def __init__(self):
        self.__orderbook = OrderBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        desc = input("description: ")
        prog_and_workload = input("programmer and workload estimate: ")
        
        try:
            prog = prog_and_workload.split(" ")[0]
            workload = int(prog_and_workload.split(" ")[1])
            self.__orderbook.add_order(desc, prog, workload)
            print("added!")
        except:
            print("erroneous input")
  

    def finished_orders(self):
        if len(self.__orderbook.finished_orders()) == 0:
            print("no finished tasks")
            return
        [print(order) for order in self.__orderbook.finished_orders()]

    def unfinished_orders(self):
        if len(self.__orderbook.unfinished_orders()) == 0:
            print("no unfinished tasks")
            return
        [print(order) for order in self.__orderbook.unfinished_orders()]

    def mark_finished(self):
        
        try:
            id = int(input("id: "))
            self.__orderbook.mark_finished(id)
            print("marked as finished")
        except:
            print("erroneous input")
    
    def programmers(self):
        [print(programmer) for programmer in self.__orderbook.programmers()]

    def programmer_status(self):
        name = input("programmer: ")
        try:
            result = self.__orderbook.status_of_programmer(name)
            print(f"tasks: finished {result[0]} not finished {result[1]}, hours: done {result[2]} scheduled {result[3]}")
        except:
            print("erroneous input")

    def execute(self):
        self.help()

        while True:
            print("")
            command = input("command: ")

            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.finished_orders()
            elif command == "3":
                self.unfinished_orders()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.programmers()
            elif command == "6":
                self.programmer_status()
            
            





application = OrderBookApplication()
application.execute()

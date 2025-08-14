from abc import ABC, abstractmethod

# --- Product ---
class Course:
    def __init__(self):
        self.name = None
        self.fee = None
        self.batches = None

    def __str__(self):
        return f"Name of Course: {self.name} and its Fee: {self.fee} (Batches: {self.batches})"


# --- Builder Interface ---
class CourseBuilder(ABC):
    def __init__(self):
        self.course = Course()

    @abstractmethod
    def set_name(self): pass

    @abstractmethod
    def set_fee(self): pass

    @abstractmethod
    def set_batches(self): pass

    def get_course(self):
        return self.course


# --- Concrete Builders ---
class DSABuilder(CourseBuilder):
    def set_name(self): self.course.name = "DSA"
    def set_fee(self): self.course.fee = 8000
    def set_batches(self): self.course.batches = 5

class SDEBuilder(CourseBuilder):
    def set_name(self): self.course.name = "SDE"
    def set_fee(self): self.course.fee = 10000
    def set_batches(self): self.course.batches = 4

class STLBuilder(CourseBuilder):
    def set_name(self): self.course.name = "STL"
    def set_fee(self): self.course.fee = 5000
    def set_batches(self): self.course.batches = 7


# --- Director ---
class Director:
    def __init__(self, builder: CourseBuilder):
        self.builder = builder

    def construct_course(self):
        self.builder.set_name()
        self.builder.set_fee()
        self.builder.set_batches()
        return self.builder.get_course()


# --- Usage ---
if __name__ == "__main__":
    dsa_course = Director(DSABuilder()).construct_course()
    sde_course = Director(SDEBuilder()).construct_course()
    stl_course = Director(STLBuilder()).construct_course()

    print(dsa_course)
    print(sde_course)
    print(stl_course)

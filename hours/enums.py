from django.utils.translation import pgettext_lazy
from enumfields import Enum


class State(Enum):
    OPEN = "open"
    CLOSED = "closed"
    UNDEFINED = "undefined"
    SELF_SERVICE = "self_service"
    WITH_KEY = "with_key"
    WITH_RESERVATION = "with_reservation"
    OPEN_AND_RESERVABLE = "open_and_reservable"
    WITH_KEY_AND_RESERVATION = "with_key_and_reservation"
    ENTER_ONLY = "enter_only"
    EXIT_ONLY = "exit_only"
    WEATHER_PERMITTING = "weather_permitting"
    NOT_IN_USE = "not_in_use"
    MAINTENANCE = "maintenance"
    RESERVED = "reserved"
    BY_APPOINTMENT = "by_appointment"

    class Labels:
        OPEN = pgettext_lazy("State", "Open")
        CLOSED = pgettext_lazy("State", "Closed")
        UNDEFINED = pgettext_lazy("State", "Undefined")
        SELF_SERVICE = pgettext_lazy("State", "Self service")
        WITH_KEY = pgettext_lazy("State", "With key")
        WITH_RESERVATION = pgettext_lazy("State", "With reservation")
        OPEN_AND_RESERVABLE = pgettext_lazy("State", "Open and reservable")
        WITH_KEY_AND_RESERVATION = pgettext_lazy("State", "With key and reservation")
        ENTER_ONLY = pgettext_lazy("State", "Enter only")
        EXIT_ONLY = pgettext_lazy("State", "Exit only")
        WEATHER_PERMITTING = pgettext_lazy("State", "Weather permitting")
        NOT_IN_USE = pgettext_lazy("State", "Not in use")
        MAINTENANCE = pgettext_lazy("State", "Maintenance")
        RESERVED = pgettext_lazy("State", "Reserved")
        BY_APPOINTMENT = pgettext_lazy("State", "By appointment")

    @classmethod
    def open_states(cls):
        return [
            cls.OPEN,
            cls.SELF_SERVICE,
            cls.WITH_KEY,
            cls.WITH_RESERVATION,
            cls.OPEN_AND_RESERVABLE,
            cls.WITH_KEY_AND_RESERVATION,
            cls.ENTER_ONLY,
            cls.WEATHER_PERMITTING,
            cls.RESERVED,
            cls.BY_APPOINTMENT,
        ]


class ResourceType(Enum):
    UNIT = "unit"
    SUBSECTION = "section"
    SPECIAL_GROUP = "special_group"
    CONTACT = "contact"
    ONLINE_SERVICE = "online_service"
    SERVICE = "service"
    SERVICE_CHANNEL = "service_channel"
    SERVICE_AT_UNIT = "service_at_unit"
    RESERVABLE = "reservable"
    BUILDING = "building"
    AREA = "area"
    ENTRANCE = "entrance_or_exit"

    class Labels:
        UNIT = pgettext_lazy("ResourceType", "Unit")
        SUBSECTION = pgettext_lazy("ResourceType", "Section")
        SPECIAL_GROUP = pgettext_lazy("ResourceType", "Special group")
        CONTACT = pgettext_lazy("ResourceType", "Contact email or phone number")
        ONLINE_SERVICE = pgettext_lazy("ResourceType", "Online service")
        SERVICE = pgettext_lazy("ResourceType", "Service")
        SERVICE_CHANNEL = pgettext_lazy("ResourceType", "Service channel")
        SERVICE_AT_UNIT = pgettext_lazy("ResourceType", "Service at unit")
        RESERVABLE = pgettext_lazy("ResourceType", "Reservable resource")
        BUILDING = pgettext_lazy("ResourceType", "Building")
        AREA = pgettext_lazy("ResourceType", "Area")
        ENTRANCE = pgettext_lazy("ResourceType", "Entrance or exit")


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    class Labels:
        MONDAY = pgettext_lazy("Weekday", "Monday")
        TUESDAY = pgettext_lazy("Weekday", "Tuesday")
        WEDNESDAY = pgettext_lazy("Weekday", "Wednesday")
        THURSDAY = pgettext_lazy("Weekday", "Thursday")
        FRIDAY = pgettext_lazy("Weekday", "Friday")
        SATURDAY = pgettext_lazy("Weekday", "Saturday")
        SUNDAY = pgettext_lazy("Weekday", "Sunday")

    @classmethod
    def business_days(cls):
        return [cls.MONDAY, cls.TUESDAY, cls.WEDNESDAY, cls.THURSDAY, cls.FRIDAY]

    @classmethod
    def weekend(cls):
        return [cls.SATURDAY, cls.SUNDAY]

    @classmethod
    def from_iso_weekday(cls, iso_weekday_num):
        for member in cls.__members__.values():
            if member.value == iso_weekday_num:
                return member


class RuleContext(Enum):
    PERIOD = "period"
    YEAR = "year"
    MONTH = "month"
    # WEEK = "week"

    class Labels:
        PERIOD = pgettext_lazy("RuleContext", "Period")
        YEAR = pgettext_lazy("RuleContext", "Year")
        MONTH = pgettext_lazy("RuleContext", "Month")
        # WEEK = pgettext_lazy("RuleContext", "Week")

        # Make strings used in the Rule.as_text method findable by makemessages
        pgettext_lazy("every_rulecontext", "period")
        pgettext_lazy("every_rulecontext", "year")
        pgettext_lazy("every_rulecontext", "month")


class RuleSubject(Enum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    MONDAY = "mon"
    TUESDAY = "tue"
    WEDNESDAY = "wed"
    THURSDAY = "thu"
    FRIDAY = "fri"
    SATURDAY = "sat"
    SUNDAY = "sun"

    class Labels:
        DAY = pgettext_lazy("RuleSubject", "Day")
        WEEK = pgettext_lazy("RuleSubject", "Week")
        MONTH = pgettext_lazy("RuleSubject", "Month")
        MONDAY = pgettext_lazy("RuleSubject", "Monday")
        TUESDAY = pgettext_lazy("RuleSubject", "Tuesday")
        WEDNESDAY = pgettext_lazy("RuleSubject", "Wednesday")
        THURSDAY = pgettext_lazy("RuleSubject", "Thursday")
        FRIDAY = pgettext_lazy("RuleSubject", "Friday")
        SATURDAY = pgettext_lazy("RuleSubject", "Saturday")
        SUNDAY = pgettext_lazy("RuleSubject", "Sunday")

        # Make strings used in the Rule.as_text method findable by makemessages
        pgettext_lazy("starting_from_nth_rulesubject", "day")
        pgettext_lazy("starting_from_nth_rulesubject", "week")
        pgettext_lazy("starting_from_nth_rulesubject", "month")
        pgettext_lazy("starting_from_nth_rulesubject", "mon")
        pgettext_lazy("starting_from_nth_rulesubject", "tue")
        pgettext_lazy("starting_from_nth_rulesubject", "wed")
        pgettext_lazy("starting_from_nth_rulesubject", "thu")
        pgettext_lazy("starting_from_nth_rulesubject", "fri")
        pgettext_lazy("starting_from_nth_rulesubject", "sat")
        pgettext_lazy("starting_from_nth_rulesubject", "sun")

    def is_singular(self):
        return self in [
            self.DAY,
            self.MONDAY,
            self.TUESDAY,
            self.WEDNESDAY,
            self.THURSDAY,
            self.FRIDAY,
            self.SATURDAY,
            self.SUNDAY,
        ]

    @classmethod
    def weekday_subjects(cls):
        return [
            cls.MONDAY,
            cls.TUESDAY,
            cls.WEDNESDAY,
            cls.THURSDAY,
            cls.FRIDAY,
            cls.SATURDAY,
            cls.SUNDAY,
        ]

    def as_isoweekday(self):
        if self not in self.weekday_subjects():
            return None

        return self.weekday_subjects().index(self) + 1

    def as_weekday(self):
        if self not in self.weekday_subjects():
            return None

        return self.weekday_subjects().index(self)


class FrequencyModifier(Enum):
    EVEN = "even"
    ODD = "odd"

    class Labels:
        EVEN = pgettext_lazy("FrequencyModifier", "Even")
        ODD = pgettext_lazy("FrequencyModifier", "Odd")

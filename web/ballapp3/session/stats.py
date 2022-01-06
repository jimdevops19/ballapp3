import ballapp3.session.constants as const

# This class will calculate statistics based on the given attempts string
# 1 Represents a made shot
# 0 Represents a missed shot
class StatsManager:
    def __init__(self, attempts_str):
        self._attempts_str = attempts_str

    @property
    def attempts_str(self):
        return self._attempts_str

    @attempts_str.setter
    def attempts_str(self, value):
        self._attempts_str = value

    def all_stats(self):
        '''
        Calls all the methods within this class that has the prefix of stat_.
        Those methods should use always attempts_str
        :return:
        '''
        stats = {}
        methods_str = [method_str for method_str in dir(self) if
                       method_str.startswith('stat_') and method_str != self.all_stats.__name__]
        get_obj_reference = lambda method_str: getattr(self, method_str)
        methods_objects = list(map(get_obj_reference, methods_str))
        for method in methods_objects:
            stats[method.__name__.replace('stat_', '')] = method()

        return stats

    def made_streaks(self):
        rows = []
        counter = 0
        for attempt in self.attempts_str:
            if attempt == const.ATTEMPT_MADE:
                counter += 1
            else:
                if counter > 0:
                    rows.append(counter)
                    counter = 0
        return sorted(rows)

    def missed_streaks(self):
        rows = []
        counter = 0
        for attempt in self.attempts_str:
            if attempt == const.ATTEMPT_MISSED:
                counter += 1
            else:
                if counter > 0:
                    rows.append(counter)
                    counter = 0
        return sorted(rows)

    def stat_total_attempts(self):
        return len(self.attempts_str)

    def stat_total_made(self):
        return self.attempts_str.count(const.ATTEMPT_MADE)

    def stat_total_missed(self):
        return self.attempts_str.count(const.ATTEMPT_MISSED)

    def stat_most_in_a_row_made(self):
        try:
            return self.made_streaks()[-1]
        except IndexError:
            return None

    def stat_most_in_a_row_missed(self):
        try:
            return self.missed_streaks()[-1]
        except:
            return None

    def stat_streaks_made_list(self):
        return list(reversed(self.made_streaks()))

    def stat_streaks_missed_list(self):
        return list(reversed(self.missed_streaks()))
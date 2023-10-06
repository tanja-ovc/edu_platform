def lesson_is_fully_watched(obj):
    time_watched = obj.time_watched
    lesson_length = obj.lesson.length
    if (time_watched / lesson_length) < 0.8:
        return False
    return True

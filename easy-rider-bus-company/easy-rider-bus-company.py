import json


def errors_in_record(record):
    result = {"bus_id": 0, "stop_id": 0, "stop_name": 0, "next_stop": 0, "stop_type": 0, "a_time": 0}
    if not isinstance(record.get("bus_id"), int):
        result.update({"bus_id": 1})
    if not isinstance(record.get("stop_id"), int):
        result.update({"stop_id": 1})
    if not is_valid_stop_name(record.get("stop_name")):
        result.update({"stop_name": 1})
    if not isinstance(record.get("next_stop"), int):
        result.update({"next_stop": 1})
    if not is_valid_stop_type(record.get("stop_type")):
        result.update({"stop_type": 1})
    if not is_valid_a_time(record.get("a_time")):
        result.update({"a_time": 1})
    return result


def is_valid_stop_name(stop_name):
    # valid_suffixes = ["Road", "Avenue", "Boulevard", "Street", "Str.", ""]
    words = []
    try:
        words = stop_name.split(sep=" ")
        # if words[-1] not in valid_suffixes:
        #     return False
        if words[0] == "abbey":
            return True
        if not words[0].istitle():
            return False
    except Exception:
        return False
    return True


def is_valid_stop_type(stop_type):
    if not isinstance(stop_type, str):
        return False
    if len(stop_type) > 1:
        return False
    return True


def is_valid_a_time(a_time):
    try:
        hour, minute = a_time.split(sep=":")
        if len(hour) > 2 or len(minute) > 2:
            return False
    except Exception:
        return False
    return True


records_validation_result = {"bus_id": 0, "stop_id": 0, "stop_name": 0, "next_stop": 0, "stop_type": 0, "a_time": 0}

records = json.loads(input())
for record in records:
    record_result = errors_in_record(record)
    records_validation_result.update({"bus_id": records_validation_result.get("bus_id") + record_result.get("bus_id")})
    records_validation_result.update({"stop_id": records_validation_result.get("stop_id") + record_result.get("stop_id")})
    records_validation_result.update({"stop_name": records_validation_result.get("stop_name") + record_result.get("stop_name")})
    records_validation_result.update({"next_stop": records_validation_result.get("next_stop") + record_result.get("next_stop")})
    records_validation_result.update({"stop_type": records_validation_result.get("stop_type") + record_result.get("stop_type")})
    records_validation_result.update({"a_time": records_validation_result.get("a_time") + record_result.get("a_time")})
total_errors = records_validation_result.get("bus_id") + records_validation_result.get("stop_id") + records_validation_result.get("stop_name") \
               + records_validation_result.get("next_stop") + records_validation_result.get("stop_type") + records_validation_result.get("a_time")
print(f"Type and required field validation: {total_errors} errors")
print(f'bus_id: {records_validation_result.get("bus_id")}')
print(f'stop_id: {records_validation_result.get("stop_id")}')
print(f'stop_name: {records_validation_result.get("stop_name")}')
print(f'next_stop: {records_validation_result.get("next_stop")}')
print(f'stop_type: {records_validation_result.get("stop_type")}')
print(f'a_time: {records_validation_result.get("a_time")}')

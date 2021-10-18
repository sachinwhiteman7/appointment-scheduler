from rest_framework.serializers import ModelSerializer, ValidationError

from timeslots.models import TimeSlot


class TimeSlotSerializer(ModelSerializer):
    """
    Serializer to represent a Timeslot serializer.
    """
    class Meta:
        model = TimeSlot
        fields = '__all__'

    def validate_start_time(self, start_time):
        if start_time.minute != 0:
            raise ValidationError("Please keep the minutes to 0")
        return start_time

    def validate_end_time(self, end_time):
        if end_time.minute != 0:
            raise ValidationError("Please keep the minutes to 0")
        return end_time

    def validate(self, data):
        if data['start_time'] >= data['end_time']:
            raise ValidationError("End time must be greater than start time.")
        return data

    def create(self, validated_data):
        user = validated_data.get('user')
        start_time = validated_data.get('start_time')
        end_time = validated_data.get('end_time')
        time_slot = None
        while start_time < end_time:
            current_end_time = start_time.replace(start_time.hour + 1)
            time_slot = TimeSlot(
                user=user,
                start_time=start_time,
                end_time=current_end_time
            )
            time_slot.save()
            start_time = current_end_time
        return time_slot




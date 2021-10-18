from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.models import User
from timeslots.models import TimeSlot


class CommonTimeSlotsApiView(APIView):
    """
    API to get the common timeslots for a interviewer and a candidate
    """
    def get(self, request, *args, **kwargs):
        """
        list all available preference questions with answers
        """

        data = request.data
        interviewer_id = data.get('interviewer_id')
        candidate_id = data.get('candidate_id')
        if not User.objects.filter(id=interviewer_id).exists():
            return Response(
                data={"error": "No Interviewer found for the given ID."},
                status=status.HTTP_404_NOT_FOUND
            )

        if not User.objects.filter(id=candidate_id).exists():
            return Response(
                data={"error": "No Candidate found for the given ID."},
                status=status.HTTP_404_NOT_FOUND
            )

        interviewer_slots = TimeSlot.objects.filter(
            user__id=interviewer_id
        ).values_list('start_time', 'end_time')

        candidate_slots = TimeSlot.objects.filter(
            user__id=candidate_id
        ).values_list('start_time', 'end_time')

        common_time_slots = [(slot[0].hour, slot[1].hour) for slot in interviewer_slots if slot in candidate_slots]
        if not common_time_slots:
            return Response(
                data={"error": "No common timeslots available"},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            data=common_time_slots,
            status=status.HTTP_200_OK
        )

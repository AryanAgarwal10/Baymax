from report.models import Report

def last_submitted_report(user):
        # request=self.context.get('request')
        # print("BABA",request.user)
        reports=Report.objects.filter(owner=user.id).order_by('-submited')
        if reports.exists():
            last_submitted = reports.first().submited
            return last_submitted
        else:
            return None
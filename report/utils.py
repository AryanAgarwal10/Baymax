from report.models import Report

def last_submitted_report(self):
        request=self.context.get('request')
        reports=Report.objects.filter(owner_id=request.user.id).order_by('-submited')
        if reports.exists():
            last_submitted = reports.first().submited
            return last_submitted
        else:
            return None
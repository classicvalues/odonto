import datetime
from odonto.odonto_submissions.serializers import translate_to_bdcs1
from fp17 import treatments


def annotate(bcds1):
    bcds1.patient.surname = "HAMSTEAD"
    bcds1.patient.forename = "MONICA"
    bcds1.patient.address = ["28 HIGH STREET"]
    bcds1.patient.sex = 'F'
    bcds1.patient.date_of_birth = datetime.date(1989, 7, 27)

    bcds1.date_of_acceptance = datetime.date(2017, 4, 1)
    bcds1.date_of_completion = datetime.date(2017, 4, 1)

    bcds1.patient_charge_pence = 5630

    # Treatments: "Fillings x 1, Recall Interval (9172 12), Ethnic Origin 11"
    bcds1.treatments = [
        treatments.TREATMENT_CATEGORY(2),
        treatments.PERMANENT_FILLINGS(1),
        treatments.RECALL_INTERVAL(12),
        treatments.ETHNIC_ORIGIN_11_OTHER_ASIAN_BACKGROUND,
    ]

    return bcds1


def from_model(bcds1, patient, episode):
    demographics = patient.demographics()
    demographics.surname = "HAMSTEAD"
    demographics.first_name = "MONICA"
    demographics.house_number_or_name = "28"
    demographics.street = "HIGH STREET"
    demographics.sex = "Female"
    demographics.date_of_birth = datetime.date(1989, 7, 27)
    demographics.ethnicity = "Other asian background"
    demographics.save()

    episode.fp17treatmentcategory_set.update(
        treatment_category="Band 2",
    )
    episode.fp17recall_set.update(
        number_of_months=12
    )
    episode.fp17exemptions_set.update(
        patient_charge_collected=56.30
    )

    episode.fp17clinicaldataset_set.update(
        permanent_fillings=1
    )
    episode.fp17incompletetreatment_set.update(
        date_of_acceptance=datetime.date(2017, 4, 1),
        completion_or_last_visit=datetime.date(2017, 4, 1)
    )

    translate_to_bdcs1(bcds1, episode)

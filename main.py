from fastapi import FastAPI, HTTPException, status
import json
import base64

app = FastAPI(
        title="AI-MD",
        description="AI-MD",
       )

@app.get("/")
def read_root(
        results: str = None,
        error: str = None,
):
    if results:
        try:
            result_ascii = base64.b64decode(results)
            result_json = json.loads(result_ascii)

            session_id = result_json.get("sessionId")
            field_mapping = {
                "blood_pressure_systolic": "BP_SYSTOLIC",
                "blood_pressure_diastolic": "BP_DIASTOLIC",
                "heart_rate_change": "HRV_SDNN",
                "stress_index": "MSI",
                "vascular_capacity": "BP_TAU",
                "respiration": "BR_BPM",
                "heart_disease_risk": "BP_HEART_ATTACK",
                "hypertension_risk": "HPT_RISK_PROB",
                "hypercholesteremia_risk": "HDLTC_RISK_PROB",
                "hypertriglyceridemia_risk": "TG_RISK_PROB",
                "hba1c": "HBA1C_RISK_PROB",
                "blood_glucose": "MFBG_RISK_PROB",
                "diabetes_risk": "DBT_RISK_PROB",
                "body_mass_index": "BMI_CALC",
                "overall_wellness": "HEALTH_SCORE",
                "pulse_rate": "HR_BPM",
                "face_skin_age": "AGE",
                "stroke_risk": "BP_STROKE",
                "cardiovascular_risk": "BP_CVD",
                "cardiac_workload": "BP_RPP",
                "waist_to_height_ratio": "WAIST_TO_HEIGHT",
                "body_shape_index": "ABSI",
                "estimated_height": "HEIGHT",
                "estimated_weight": "WEIGHT",
                "waist_circumference": "WAIST_CIRCUM",
                "fatty_liver_disease_risk": "FLD_RISK_PROB",
                "overall_health_score": "HEALTH_SCORE",
                "mental_health_score": "MENTAL_SCORE",
                "physical_health_score": "PHYSICAL_SCORE",
                "physiological_health_score": "PHYSIO_SCORE",
                "disease_risk_score": "RISKS_SCORE",
                "vital_score": "VITAL_SCORE",
                "metabolic_health_score": "OVERALL_METABOLIC_RISK_PROB",
                "irregular_heartbeat_count": "IHB_COUNT",
            }

            for key in field_mapping:
                if field_mapping[key] is not None:
                    field_mapping[key] = result_json.get(field_mapping[key])

            json_body = {
                "vitals": field_mapping,
            }
            return json_body
        except Exception as e:
            print(e)
            raise HTTPException(detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif error:
        raise HTTPException(detail=str(error), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return {"result": "Hello, DOCKTOR CONNECT!"}

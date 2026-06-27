from downloader import download_audio
from transcriber import transcribe_audio
from claim_extractor import classify
from search import search_web
from verifier import verify
import json


def run_pipeline(video_url):

    # Download audio
    latest_audio = download_audio(video_url)

    # Transcribe
    transcript = transcribe_audio(latest_audio)

    # Extract and classify claims
    classification_output = classify(transcript)

    try:
        classified = json.loads(classification_output)
    except Exception:
        classified = []

    results = []

    for item in classified:

        sentence = item["sentence"]
        category = item["category"]

        evidence = None
        verification = None

        if category == "FACT":

            evidence = search_web(sentence)

            if evidence:

                combined_evidence = ""

                for i, result in enumerate(evidence[:3], start=1):

                    combined_evidence += f"""
Source {i}

Title:
{result.get("title", "")}

URL:
{result.get("url", "")}

Content:
{result.get("content", "")}

----------------------------------------
"""

                verification = verify(
                    sentence,
                    combined_evidence
                )

        results.append({
            "sentence": sentence,
            "category": category,
            "evidence": evidence,
            "verification": verification
        })

    return {
        "transcript": transcript,
        "results": results
    }
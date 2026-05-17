def get_hotlines(country: str = "global") -> list:
    """
    Returns crisis hotlines based on country.
    Defaults to global if country not found.
    """

    hotlines = {
        "pakistan": [
            {
                "name": "Umang Mental Health Helpline",
                "number": "0317-4288665",
                "available": "24/7",
                "note": "Free, confidential mental health support in Urdu and English"
            },
            {
                "name": "Rozan Counseling Center",
                "number": "051-2890505",
                "available": "Mon-Sat 9am-5pm",
                "note": "Professional counseling and crisis support"
            },
            {
                "name": "Rescue Emergency",
                "number": "1122",
                "available": "24/7",
                "note": "For immediate physical emergencies"
            }
        ],
        "usa": [
            {
                "name": "988 Suicide & Crisis Lifeline",
                "number": "988",
                "available": "24/7",
                "note": "Call or text — free and confidential"
            },
            {
                "name": "Crisis Text Line",
                "number": "Text HOME to 741741",
                "available": "24/7",
                "note": "Text-based crisis support"
            }
        ],
        "uk": [
            {
                "name": "Samaritans",
                "number": "116 123",
                "available": "24/7",
                "note": "Free to call, confidential"
            },
            {
                "name": "CALM",
                "number": "0800 58 58 58",
                "available": "5pm-midnight daily",
                "note": "Campaign Against Living Miserably"
            }
        ],
        "pakistan": [
            {
                "name": "police",
                "number": "15",
                "available": "24/7",
                "note": "Free to call, confidential"
            },
            {
                "name": "Fire Brigade",
                "number": "16",
                "available": "24/7",
                "note": "Free to call, confidential"
            },
            {
                "name": "Women Helpline",
                "number": "1043",
                "available": "24/7",
                "note": "Campaign to protect women from violence and abuse"
            }
        ],
        "global": [
            {
                "name": "International Association for Suicide Prevention",
                "number": "https://www.iasp.info/resources/Crisis_Centres/",
                "available": "24/7",
                "note": "Find your local crisis center"
            },
            {
                "name": "Crisis Text Line (US/UK/CA/IE)",
                "number": "Text HOME to 741741",
                "available": "24/7",
                "note": "Text-based support"
            }
        ]
    }

    result = hotlines.get(country.lower(), hotlines["global"])
    return result


def format_hotlines(hotlines: list) -> str:
    lines = ["📞 **Crisis Hotlines — You are not alone:**\n"]
    for h in hotlines:
        lines.append(f"  🔹 **{h['name']}**")
        lines.append(f"     Number : {h['number']}\n")
        lines.append(f"     Hours  : {h['available']}\n")
        lines.append(f"     Note   : {h['note']}\n")
    return "\n".join(lines)
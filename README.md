# Incident Response Playbook

An interactive Python tool that guides a SOC analyst through a step-by-step incident response process for three common attack types. Tracks completed steps and generates a closure report.

## Incident Types Covered
- **Phishing Attack** — Email-based social engineering
- **Ransomware Attack** — File encryption and extortion
- **Unauthorized Access** — Credential compromise and intrusion

## IR Phases (per incident)
1. **Identification** — Confirm and scope the incident
2. **Containment** — Stop the bleeding
3. **Eradication** — Remove the threat
4. **Recovery** — Restore normal operations
5. **Lessons Learned** — Document and improve

## How to run

```
python ir_playbook.py
```

## Example output

```
=======================================================
  INCIDENT RESPONSE PLAYBOOK
  Select incident type:
  1. Phishing Attack
  2. Ransomware Attack
  3. Unauthorized Access

  Enter 1, 2, or 3: 1

--- IDENTIFICATION ---
  Confirm the report — who received it and when?
  [C/S] > C
  ...

=======================================================
  INCIDENT RESPONSE SUMMARY
  Incident:  Phishing Attack
  Completed: 22/25 steps (88%)
  STATUS: Mostly resolved. Complete skipped steps.
=======================================================
```

## Why this matters

Incident response is one of the most critical skills in cybersecurity. SOC analysts and IR teams follow structured playbooks like this to ensure nothing is missed during a live incident. Based on the NIST SP 800-61 incident handling framework.

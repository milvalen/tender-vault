---
title: Speech recognition services
type: reference
status: proposed
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: aistudio.yandex.ru (SpeechKit pricing), developers.sber.ru (SaluteSpeech tariffs, hints), tbank.ru/software/voicekit, vibecoding.ru, cloud.vk.ru/cloud-voice, cloud.google.com/speech/pricing, help.openai.com (supported countries), alphacephei.com/vosk/android [Claude] 2026-11-13
parent: 20-device.md
---

# Speech recognition services

Comparison for the [voice order notebook](functions.md#2-voice-order-notebook). Voice runs in the cloud through the server's phone `[A]` 2026-11-13, see the [decision log](../70-decisions/70-decisions.md#2026-11-13-voice-runs-in-the-cloud-through-the-phone).

Limit: web research only `[Claude]` 2026-11-13. No service was tested on real speech. Prices come from vendor pages and reviews; some reviews do not agree. Check the vendor page before you pay.

## What the device needs

1. Russian speech, short phrases of 3 to 6 s: "table seven, seat two, carbonara without bacon".
2. Noise of the restaurant floor.
3. Menu words: dish names, often borrowed words. Word hints or a custom vocabulary help.
4. Streaming or a fast short request: the server waits for the result.
5. Access and payment from Russia for a private person.

## Comparison

| Service | Price for recognition | Billing step | Menu words | Access from Russia |
|---|---|---|---|---|
| Yandex SpeechKit | about 0.16 RUB for 15 s, streaming or synchronous (about 0.65 RUB/min) | 15 s, rounded up | not checked `[?]` | yes |
| T-Bank VoiceKit | 0.60 RUB/min streaming, 0.378 RUB/min file, without VAT | 1 s | not checked `[?]` | yes; account for a private person not checked `[?]` |
| SaluteSpeech (Sber) | private person: package of 1,000 min for 1,200 RUB, 1 month. Company: 0.6 RUB/min | package | yes: `words` hints, up to 100 | yes. The free plan for private persons stopped on 2026-07-15 |
| VK Cloud Voice | not published | not published | not checked `[?]` | yes |
| Google Speech-to-Text (Chirp) | 0.016 USD/min | not checked | yes: phrase hints | payment from Russia not available `[?]` |
| OpenAI transcription | 0.003 to 0.006 USD/min `[?]` | not checked | text prompt | no: Russia is not a supported country |
| Vosk on the phone (offline, not cloud) | free, open source | — | yes: a word list for the recognizer | yes, no account |

## Cost per shift

Estimate `[?]`: 60 voice entries per shift, 5 s each, 5 min of speech in total.

| Service | Cost per shift |
|---|---|
| Yandex SpeechKit | about 10 RUB: each 5 s phrase is billed as 15 s |
| T-Bank VoiceKit | about 3 RUB without VAT |
| SaluteSpeech, private person | 1,200 RUB per month for the package, used only in part |
| Vosk on the phone | 0 RUB |

The price does not decide the choice. The accuracy on the floor decides it.

## Findings

1. Google and OpenAI are not practical: payment or access from Russia is a problem.
2. Yandex SpeechKit, T-Bank VoiceKit and SaluteSpeech are the real cloud candidates.
3. SaluteSpeech has documented word hints. These help with dish names.
4. Vosk runs offline on an Android phone. It needs no internet and no account. This keeps concept principle 1 fully, but it is usually less accurate than a cloud service `[?]`.

## Proposed test

Status: proposed `[Claude]` 2026-11-13. Artemy decides.

1. Record 30 order phrases on the floor with the phone, or in a noisy room. Use real menu items. Keep the recordings in `_private/`.
2. Write the correct text for each phrase.
3. Send the same recordings to 2 or 3 candidates: Yandex SpeechKit, SaluteSpeech with the menu as hints, and Vosk.
4. Count the phrases where the table, the seat and the dish are all correct.
5. Choose the service with the best count. Write the result and the decision in the [decision log](../70-decisions/70-decisions.md).

[Parent](20-device.md)

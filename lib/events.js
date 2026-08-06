export const EVENTS = [
  {
    slug: "model-united-nations",
    name: "Model United Nations",
    tagline: "Think Globally, Act Diplomatically",
    team: "Individual Participation",
    fee: "₹100 per delegate",
    dates: ["Round 1 — 26 Oct 2025", "Round 2 — 2 Nov 2025"],
    accent: "#ff7a59",
    blurb:
      "Step into the shoes of a global diplomat. Delegates represent nations across simulated UN committees, drafting resolutions, forging alliances, and defending their country's stance under pressure.",
    highlights: [
      "Two rounds of committee sessions with rising stakes",
      "Awards for Best Delegate, Diplomacy, and Verbal skills",
      "Position papers required ahead of Round 1",
      "Open to first-time and experienced delegates alike",
    ],
  },
  {
    slug: "ex-quizit",
    name: "Ex-Quizit",
    tagline: "Seeking Horizons Beyond Semblance",
    team: "1–2 Members",
    fee: "₹50 per team",
    dates: ["Round 1 — 2 Nov 2025", "Round 2 — 5 Nov 2025"],
    accent: "#ffb703",
    blurb:
      "A fast-paced general knowledge and science quiz that rewards curiosity as much as recall. Teams race through rapid-fire, visual, and buzzer rounds to claim the crown.",
    highlights: [
      "Prelims followed by a live buzzer finale",
      "Rounds spanning science, current affairs, and pop culture",
      "Buzzer system finals for the top 6 teams",
      "Great for duos who love thinking on their feet",
    ],
  },
  {
    slug: "math-a-maze",
    name: "Math-a-Maze",
    tagline: "Labyrinth of Logic",
    team: "Individual Participation",
    fee: "₹30 per member",
    dates: ["Round 1 — 2 Nov 2025", "Round 2 — 5 Nov 2025"],
    accent: "#06d6a0",
    blurb:
      "Navigate a maze of puzzles, riddles, and logical traps designed to test pattern recognition and mathematical agility under the clock.",
    highlights: [
      "Timed puzzle rounds of increasing difficulty",
      "No calculators — pure logic and speed",
      "Individual leaderboard tracked across both rounds",
      "Perfect for young mathletes who love a challenge",
    ],
  },
  {
    slug: "junior-science-olympiad",
    name: "Junior Science Olympiad",
    tagline: "Catalyzing Curiosity, Igniting Imagination",
    team: "Individual Participation",
    fee: "₹30 per member",
    dates: ["Round 1 — 2 Nov 2025", "Round 2 — 5 Nov 2025"],
    accent: "#118ab2",
    blurb:
      "A written and applied science olympiad covering physics, chemistry, and biology fundamentals — built to spark scientific temperament in young minds.",
    highlights: [
      "Objective-type Round 1, applied Round 2",
      "Syllabus aligned to middle and high school science",
      "Medals for top 3 across two age categories",
      "Sample papers shared one week before Round 1",
    ],
  },
  {
    slug: "modelothon",
    name: "Modelothon",
    tagline: "Build Brilliance, Cross Excellence",
    team: "1–3 Members",
    fee: "₹60 per team",
    dates: ["5 Nov 2025"],
    accent: "#ef476f",
    blurb:
      "Design and build a working or static model that solves a real-world problem. Judged on innovation, craftsmanship, and the clarity of your pitch.",
    highlights: [
      "Bring your own materials — basic tools provided",
      "5-minute pitch and live Q&A with judges",
      "Working models score bonus points",
      "Open theme — showcase any field of science",
    ],
  },
  {
    slug: "catapultikon",
    name: "Catapultikon",
    tagline: "Storm The Gates, Seize The Crown",
    team: "1–3 Members",
    fee: "₹60 per team",
    dates: ["5 Nov 2025"],
    accent: "#8338ec",
    blurb:
      "Engineer a catapult from scratch and battle it out for accuracy and range. Physics meets medieval flair in this hands-on build competition.",
    highlights: [
      "On-spot build using provided raw materials",
      "Scoring on accuracy, range, and reload speed",
      "Bonus points for structural creativity",
      "Safety briefing mandatory before launch trials",
    ],
  },
  {
    slug: "arduino-expo",
    name: "Arduino Expo",
    tagline: "Ideate. Invent. Inspire",
    team: "1–3 Members",
    fee: "₹60 per team",
    dates: ["5 Nov 2025"],
    accent: "#3a86ff",
    blurb:
      "Showcase an Arduino-powered project — from smart sensors to mini robots. A stage for young innovators to demo real, functioning tech.",
    highlights: [
      "Bring your own pre-built Arduino project",
      "Live demo and technical Q&A with judges",
      "Judged on functionality, originality, and utility",
      "Power outlets and demo tables provided on-site",
    ],
  },
];

export function getEventBySlug(slug) {
  return EVENTS.find((e) => e.slug === slug);
}

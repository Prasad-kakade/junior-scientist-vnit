"use client";

import Link from "next/link";
import { EVENTS } from "@/lib/events";
import { MapPin, Trophy, CalendarDays, Sparkles, ArrowDown, Users, IndianRupee, Phone } from "lucide-react";

export default function HomePage() {
  return (
    <div style={{ minHeight: "100vh", background: "#0b0d17", color: "#f4f4f8", fontFamily: "'Segoe UI', system-ui, sans-serif" }}>
      {/* Hero */}
      <header style={{
        padding: "72px 24px 56px",
        textAlign: "center",
        background: "radial-gradient(circle at 50% 0%, #1c1f3a 0%, #0b0d17 70%)",
        borderBottom: "1px solid #23263f",
      }}>
        <div style={{ display: "inline-flex", alignItems: "center", gap: 8, padding: "6px 16px", borderRadius: 999, background: "#161933", border: "1px solid #2c2f52", fontSize: 13, letterSpacing: 1, color: "#a5a9e8", marginBottom: 24 }}>
          <Sparkles size={14} /> AXIS&nbsp;'26 &middot; VNIT NAGPUR
        </div>
        <h1 style={{ fontSize: "clamp(2.4rem, 6vw, 4.2rem)", fontWeight: 800, margin: 0, letterSpacing: -1, background: "linear-gradient(90deg,#ff7a59,#ffb703,#06d6a0,#3a86ff)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent" }}>
          Junior Scientist
        </h1>
        <p style={{ fontSize: 18, color: "#c4c6e0", marginTop: 12, fontStyle: "italic" }}>
          Where curious minds become tomorrow's innovators
        </p>
        <div style={{ display: "flex", gap: 24, justifyContent: "center", flexWrap: "wrap", marginTop: 28, fontSize: 14, color: "#9ea1c9" }}>
          <span style={{ display: "flex", alignItems: "center", gap: 6 }}><CalendarDays size={16} /> 26 Oct, 2 &amp; 5 Nov 2025</span>
          <span style={{ display: "flex", alignItems: "center", gap: 6 }}><MapPin size={16} /> VNIT, Nagpur</span>
          <span style={{ display: "flex", alignItems: "center", gap: 6, color: "#ffd166", fontWeight: 600 }}><Trophy size={16} /> Prizes worth ₹1,00,000</span>
        </div>
      </header>

      {/* Intro blurb */}
      <section style={{ maxWidth: 780, margin: "0 auto", padding: "48px 24px 8px", textAlign: "center" }}>
        <p style={{ fontSize: 16, lineHeight: 1.7, color: "#c4c6e0" }}>
          Junior Scientist is a three-day festival of ideas hosted under AXIS&nbsp;'26 at VNIT Nagpur —
          seven events spanning diplomacy, logic, engineering, and invention, built for school students
          who want to think bigger, build bolder, and compete with the best young minds in the city.
          Tap an event below to see full details and register.
        </p>
        <div style={{ display: "flex", alignItems: "center", justifyContent: "center", gap: 6, marginTop: 20, color: "#6d70a6", fontSize: 13 }}>
          <ArrowDown size={14} /> Explore the events
        </div>
      </section>

      {/* Cards grid */}
      <section style={{ maxWidth: 1100, margin: "0 auto", padding: "24px 24px 64px", display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(230px, 1fr))", gap: 20 }}>
        {EVENTS.map((ev) => (
          <Link
            key={ev.slug}
            href={`/events/${ev.slug}`}
            style={{
              textDecoration: "none",
              color: "inherit",
              display: "block",
              border: "1px solid #23263f",
              background: "#12142a",
              borderRadius: 18,
              padding: "22px 20px",
              transition: "transform 0.15s ease, border-color 0.15s ease",
            }}
          >
            <div style={{
              width: 46, height: 46, borderRadius: 12, display: "flex", alignItems: "center", justifyContent: "center",
              background: `${ev.accent}22`, color: ev.accent, marginBottom: 16, fontWeight: 700, fontSize: 18,
            }}>
              {ev.name.charAt(0)}
            </div>
            <h3 style={{ margin: "0 0 6px", fontSize: 17, fontWeight: 700 }}>{ev.name}</h3>
            <p style={{ margin: "0 0 14px", fontSize: 13, color: "#9497c2", fontStyle: "italic" }}>"{ev.tagline}"</p>
            <div style={{ fontSize: 12, color: "#7a7da8", display: "flex", flexDirection: "column", gap: 4 }}>
              <span style={{ display: "flex", alignItems: "center", gap: 6 }}><Users size={12} /> {ev.team}</span>
              <span style={{ display: "flex", alignItems: "center", gap: 6 }}><IndianRupee size={12} /> {ev.fee}</span>
            </div>
          </Link>
        ))}
      </section>

      {/* Footer */}
      <footer style={{ borderTop: "1px solid #23263f", padding: "28px 24px", textAlign: "center", fontSize: 13, color: "#7a7da8" }}>
        <p style={{ display: "flex", alignItems: "center", justifyContent: "center", gap: 6, marginBottom: 10 }}>
          <MapPin size={14} /> VNIT, Nagpur &nbsp;·&nbsp; Visvesvaraya National Institute of Technology
        </p>
        <p style={{ display: "flex", alignItems: "center", justifyContent: "center", gap: 6, flexWrap: "wrap" }}>
          <Phone size={13} /> Aman 8591665502 &nbsp;·&nbsp; Manaswi 8421676578 &nbsp;·&nbsp; Taha 8928240729 &nbsp;·&nbsp; Soumya 8956015115
        </p>
      </footer>
    </div>
  );
}

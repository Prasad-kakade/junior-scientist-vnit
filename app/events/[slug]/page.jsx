import { EVENTS, getEventBySlug } from "@/lib/events";
import { notFound } from "next/navigation";

// Pre-render a page for every event slug at build time
export function generateStaticParams() {
  return EVENTS.map((ev) => ({ slug: ev.slug }));
}

export default function EventPage({ params }) {
  const event = getEventBySlug(params.slug);

  if (!event) {
    notFound();
  }

  return (
    <div style={{ minHeight: "100vh", background: "#0b0d17", color: "#f4f4f8" }}>
      {/*
        Intentionally left blank.
        This page will hold the full registration flow for: {event.name}
        Reachable at /events/{event.slug}
      */}
    </div>
  );
}

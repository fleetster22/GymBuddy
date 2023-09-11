import { useState } from "react";

const faqs = [
  {
    title: "How does the app help me?",
    text: "The app is here to help you find exercises to improve your workout efficiency.",
  },
  {
    title: "What is the purpose of this fitness app?",
    text: "The purpose of this fitness app is to help users track and improve their overall fitness levels through a range of features designed to enhance their physical and mental well being.",
  },
  {
    title: "Can this fitness app be customized according to individual goals?",
    text: "Yes, this fitness app offers personalized fitness plaans and customizable workouts based on individual goals such as weight loss, muscle gain, cardiovascular fitness, or improving flexibility.",
  },
  {
    title:
      "How can users track their progress and set goals using this fitness app?",
    text: "This fitness app features an intuitive dashboard where users can monitor their progress over time with the workout history functionality. ",
  },
];

export default function Questions() {
  return (
    <div>
      <Accordion data={faqs} />
    </div>
  );
}

function Accordion({ data }) {
  const [curOpen, setCurOpen] = useState(null);

  return (
    <div className="accordion">
      {data.map((el, i) => (
        <AccordionItem
          curOpen={curOpen}
          onOpen={setCurOpen}
          title={el.title}
          num={i}
          key={el.title}
        >
          {el.text}
        </AccordionItem>
      ))}
    </div>
  );
}

function AccordionItem({ num, title, curOpen, onOpen, children }) {
  const isOpen = num === curOpen;

  function handleToggle() {
    onOpen(isOpen ? null : num);
  }
  return (
    <div className={`item ${isOpen ? "open" : ""}`} onClick={handleToggle}>
      <p className="number">{num < 9 ? `0${num + 1}` : num + 1}</p>
      <p className="title">{title}</p>
      <p className="icon">{isOpen ? "-" : "+"}</p>

      {isOpen && <div className="content-box">{children}</div>}
    </div>
  );
}

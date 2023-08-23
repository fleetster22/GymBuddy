import Button from "react-boostrap/Button";
import Card from "react-boostrap/Card";

export default function Card() {
  return (
    <Card>
      <Card.Body>
        <Card.Title>{exercise.name}</Card.Title>
        <Card.Text>{exercise.difficulty}</Card.Text>
        <Card.Text>{exercise.equipment}</Card.Text>
        <Card.Text>{exercise.instructions}</Card.Text>
        <Button variant="primary">Complete Workout</Button>
      </Card.Body>
    </Card>
  );
}

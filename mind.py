from flask import Flask, render_template, request
from dataclasses import dataclass
from typing import List
import os

app = Flask(__name__)

@dataclass
class Superpower:
    name: str
    description: str
    potential_uses: List[str]

class SuperpowerRecommender:
    @staticmethod
    def get_recommendations(brain_capacity: float) -> List[Superpower]:
        power_map = [
            (0, 10, Superpower(
                name="Basic Awareness",
                description="Foundational cognitive potential",
                potential_uses=[
                    "Improved basic decision making",
                    "Elementary problem recognition",
                    "Simple pattern detection"
                ]
            )),
            (10, 20, Superpower(
                name="Intuitive Sensing",
                description="Emerging perceptual capabilities",
                potential_uses=[
                    "Enhanced emotional understanding",
                    "Subtle environmental awareness",
                    "Basic empathy development"
                ]
            )),
            (20, 30, Superpower(
                name="Cognitive Amplification",
                description="Developing mental processing",
                potential_uses=[
                    "Accelerated learning",
                    "Improved information retention",
                    "Enhanced analytical thinking"
                ]
            )),
            (30, 40, Superpower(
                name="Mental Networking",
                description="Advanced cognitive connectivity",
                potential_uses=[
                    "Holistic problem solving",
                    "Intuitive ideation",
                    "Cross-disciplinary thinking"
                ]
            )),
            (40, 50, Superpower(
                name="Adaptive Intelligence",
                description="Dynamic cognitive flexibility",
                potential_uses=[
                    "Rapid skill acquisition",
                    "Complex scenario modeling",
                    "Innovative problem resolution"
                ]
            )),
            (50, 60, Superpower(
                name="Quantum Thinking",
                description="Multidimensional cognitive processing",
                potential_uses=[
                    "Simultaneous multiple perspective analysis",
                    "Advanced pattern recognition",
                    "Predictive reasoning"
                ]
            )),
            (60, 70, Superpower(
                name="Consciousness Expansion",
                description="Transcendent mental capabilities",
                potential_uses=[
                    "Profound empathetic connections",
                    "Intuitive universal understanding",
                    "Spontaneous knowledge integration"
                ]
            )),
            (70, 80, Superpower(
                name="Reality Perception Manipulation",
                description="Advanced consciousness engineering",
                potential_uses=[
                    "Temporal awareness",
                    "Quantum entanglement comprehension",
                    "Consciousness field interaction"
                ]
            )),
            (80, 90, Superpower(
                name="Cosmic Consciousness",
                description="Universal information network access",
                potential_uses=[
                    "Interdimensional communication",
                    "Collective intelligence participation",
                    "Existential problem solving"
                ]
            )),
            (90, 100, Superpower(
                name="Omniscient Awareness",
                description="Complete universal information integration",
                potential_uses=[
                    "Absolute knowledge synthesis",
                    "Reality creation and manipulation",
                    "Infinite potential exploration"
                ]
            ))
        ]

        # Find the appropriate power range
        for min_cap, max_cap, power in power_map:
            if min_cap <= brain_capacity < max_cap:
                return [power]
        
        return []

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    brain_capacity = 30.0  # Default value
    error_message = None

    if request.method == 'POST':
        try:
            brain_capacity = float(request.form.get('brain_capacity', 30.0))
            
            # Validate input range
            if brain_capacity < 0 or brain_capacity > 100:
                error_message = "Brain capacity must be between 0 and 100%"
            else:
                recommendations = SuperpowerRecommender.get_recommendations(brain_capacity)
        except ValueError:
            error_message = "Invalid brain capacity input. Please enter a number."

    return render_template(
        'index.html', 
        recommendations=recommendations, 
        brain_capacity=brain_capacity,
        error_message=error_message
    )

# Ensure the template directory exists
def ensure_template_directory():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    templates_dir = os.path.join(current_dir, 'templates')
    static_dir = os.path.join(current_dir, 'static')
    
    os.makedirs(templates_dir, exist_ok=True)
    os.makedirs(os.path.join(static_dir, 'css'), exist_ok=True)

if __name__ == '__main__':
    ensure_template_directory()
    app.run(debug=True)
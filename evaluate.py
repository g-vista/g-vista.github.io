#!/usr/bin/env python3
"""
Evaluation script for VideoAgent on benchmark datasets
"""

import argparse
import json
from pathlib import Path
from typing import Dict, List

from src.videoagent import VideoAgent
from src.evaluation.metrics import VideoMetrics
from src.utils.config import load_config
from src.utils.logging import setup_logger


def load_benchmark_data(dataset_path: str) -> List[Dict]:
    """Load benchmark dataset."""
    with open(dataset_path, 'r') as f:
        return json.load(f)


def evaluate_model(agent: VideoAgent, test_data: List[Dict], output_dir: str) -> Dict:
    """Evaluate VideoAgent on test dataset."""
    results = []
    metrics = VideoMetrics()
    
    for i, sample in enumerate(test_data):
        print(f"Evaluating sample {i+1}/{len(test_data)}")
        
        # Generate video
        result = agent.generate(
            prompt=sample['prompt'],
            iterations=3,
            output_path=f"{output_dir}/sample_{i}.mp4"
        )
        
        # Compute metrics
        sample_metrics = metrics.compute_all(
            video_path=result['video_path'],
            prompt=sample['prompt'],
            ground_truth=sample.get('ground_truth')
        )
        
        results.append({
            'sample_id': i,
            'prompt': sample['prompt'],
            'metrics': sample_metrics,
            'quality_score': result['quality_score']
        })
    
    # Aggregate results
    avg_metrics = {}
    for key in results[0]['metrics'].keys():
        avg_metrics[key] = sum(r['metrics'][key] for r in results) / len(results)
    
    return {
        'individual_results': results,
        'average_metrics': avg_metrics,
        'total_samples': len(results)
    }


def main():
    parser = argparse.ArgumentParser(description="Evaluate VideoAgent")
    parser.add_argument("--dataset", type=str, required=True, help="Dataset type (single_scene/multi_scene)")
    parser.add_argument("--model", type=str, default="videoagent", help="Model to evaluate")
    parser.add_argument("--config", type=str, default="configs/default.yaml", help="Config file")
    parser.add_argument("--output_dir", type=str, default="evaluation_results", help="Output directory")
    
    args = parser.parse_args()
    
    # Setup
    logger = setup_logger()
    config = load_config(args.config)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Load test data
    dataset_path = f"data/{args.dataset}_test.json"
    test_data = load_benchmark_data(dataset_path)
    
    # Initialize model
    agent = VideoAgent(config=config, logger=logger)
    
    # Run evaluation
    logger.info(f"Starting evaluation on {args.dataset} dataset")
    results = evaluate_model(agent, test_data, str(output_dir))
    
    # Save results
    results_path = output_dir / f"{args.model}_{args.dataset}_results.json"
    with open(results_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Print summary
    print(f"\nEvaluation Results for {args.model} on {args.dataset}:")
    print(f"Total samples: {results['total_samples']}")
    print("Average metrics:")
    for metric, value in results['average_metrics'].items():
        print(f"  {metric}: {value:.3f}")


if __name__ == "__main__":
    main()

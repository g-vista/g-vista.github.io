#!/usr/bin/env python3
"""
VideoAgent: A Test-Time Self-Improving Video Generation Agent
Main entry point for the VideoAgent system.
"""

import argparse
import os
from pathlib import Path

from src.videoagent import VideoAgent
from src.utils.config import load_config
from src.utils.logging import setup_logger


def main():
    parser = argparse.ArgumentParser(description="VideoAgent: Self-Improving Video Generation")
    parser.add_argument("--prompt", type=str, required=True, help="Video generation prompt")
    parser.add_argument("--iterations", type=int, default=3, help="Number of refinement iterations")
    parser.add_argument("--output", type=str, default="output.mp4", help="Output video path")
    parser.add_argument("--config", type=str, default="configs/default.yaml", help="Configuration file")
    parser.add_argument("--model", type=str, default="stable-video-diffusion", help="Base video model")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    
    args = parser.parse_args()
    
    # Setup logging
    logger = setup_logger(verbose=args.verbose)
    
    # Load configuration
    config = load_config(args.config)
    
    # Initialize VideoAgent
    logger.info("Initializing VideoAgent...")
    agent = VideoAgent(
        model=args.model,
        config=config,
        logger=logger
    )
    
    # Generate video with iterative refinement
    logger.info(f"Starting video generation with prompt: '{args.prompt}'")
    result = agent.generate(
        prompt=args.prompt,
        iterations=args.iterations,
        output_path=args.output
    )
    
    logger.info(f"Video generation completed. Output saved to: {args.output}")
    logger.info(f"Final quality score: {result['quality_score']:.3f}")
    logger.info(f"Refinement iterations: {result['iterations_used']}")


if __name__ == "__main__":
    main()

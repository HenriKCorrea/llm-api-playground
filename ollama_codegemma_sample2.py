from ollama import generate
from ollama import GenerateResponse

prefix = '''package org.apache.spark.examples

import com.intel.hibench.sparkbench.common.IOCommon
import org.apache.spark.SparkContext._
import org.apache.spark.{SparkConf, SparkContext}

/**
 * Computes the PageRank of URLs from an input file. Input file should
 * be in format of:
 * URL         neighbor URL
 * URL         neighbor URL
 * URL         neighbor URL
 * ...
 * where URL and their neighbors are separated by space(s).
 */
object LLMSparkPageRank {
  def main(args: Array[String]) {
    if (args.length < 2) {
      System.err.println("Usage: LLMSparkPageRank <input_file> <output_filename> [<iter>]")
      System.exit(1)
    }
    val sparkConf = new SparkConf().setAppName("ScalaPageRank")
    val input_path = args(0)
    val output_path = args(1)
    val iters = if (args.length > 2) args(2).toInt else 10
    val ctx = new SparkContext(sparkConf)'''

suffix = '''    val io = new IOCommon(ctx)
    io.save(output_path, ranks)
    ctx.stop()
  }
}'''

genResponse: GenerateResponse = generate(
  model='codegemma:2b-code',
  prompt=f'<|fim_prefix|>{prefix}<|fim_suffix|>{suffix}<|fim_middle|>',
  options={
    'num_predict': 128,
    'temperature': 0,
    'top_p': 0.9,
    'stop': ['<|file_separator|>'],
  },
)

print(genResponse.response)

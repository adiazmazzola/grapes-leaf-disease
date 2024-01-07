from tfx.proto import example_gen_pb2
from tfx.orchestration import pipeline
from tfx.components import ExampleGen
from tfx.components import StatisticGen
from tfx.components import ExampleValidator
from tfx.components import SchemaGen
from tfx.components import Transform
import os




census_transfor_module_file = 'census_transform.py'



def create_pipeline(
        pipeline_name,
        pipeline_root,
        data_path,
        serving_dir,
        metadata_conection_config=None,
        #beam_pipeline_args=beam_pipeline_args,
):
    components = []

    #example gen
    output = example_gen_pb2.Output(
        split_config = example_gen_pb2.SplitConfig(splits=[
            example_gen_pb2.SplitConfig.Split(name = 'train', hash_buckets = 8),
            example_gen_pb2.SplitConfig.Split(name = 'eval', hash_buckets = 2)
        ])
    )

    example_gen = ExampleGen(input_base = data_path, output_config = output )
    components.append(example_gen)

    statistic_gen = StatisticGen(examples = example_gen.output['examples'])
    components.append(statistic_gen)

    schema_gen = SchemaGen(statistics=statistic_gen.output['statistics'])
    components.append(schema_gen)

    validator = ExampleValidator(
        statistics=statistic_gen.output['statistics'],
        schema=schema_gen.output['schema']
    )
    components.append(validator)


    transform = Transform(
        example=example_gen.output['example'],
        schema=schema_gen.output['schema'],
        module_file=census_transfor_module_file
    )
    components.append(transform)

    



    return pipeline.Pipeline(
        pipeline_name=pipeline_name,
        pipeline_root=pipeline_root,
        components=components,
        metadata_conection_config=metadata_conection_config,
        beam_pipeline_args=beam_pipeline_args
    )
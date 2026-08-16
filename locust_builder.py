from seeds.builder import build_grpc_seeds_builder
from seeds.dumps import save_seeds_result, load_seeds_result
from seeds.schemas.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan, SeedCardsPlan

builder = build_grpc_seeds_builder()

result = builder.build(
    SeedsPlan(
        users=SeedUsersPlan(
            count=500,
            credit_card_accounts=SeedAccountsPlan(
                count=1,
                physical_cards=SeedCardsPlan(count=1)
            ),
        ),
    )
)

save_seeds_result(result=result, scenario="test-scenario")
print(load_seeds_result(scenario="test-scenario"))

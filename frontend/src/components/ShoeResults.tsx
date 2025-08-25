import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { ExternalLink, Star, DollarSign, Palette, Ruler } from "lucide-react";

interface ShoeRecommendation {
  name: string;
  category: string;
  price: string | null;
  product_code: string | null;
  colors: string[];
  sizes: string[];
  availability: string | null;
  url: string;
  rank: number;
  size_match: boolean;
}

interface ShoeResultsProps {
  recommendations: ShoeRecommendation[];
}

export function ShoeResults({ recommendations }: ShoeResultsProps) {
  if (!recommendations || recommendations.length === 0) {
    return (
      <Card className="w-full max-w-4xl mx-auto mt-8 shadow-card">
        <CardContent className="flex items-center justify-center h-32">
          <p className="text-muted-foreground">No recommendations found. Try adjusting your search criteria.</p>
        </CardContent>
      </Card>
    );
  }

  return (
    <div className="w-full max-w-6xl mx-auto mt-8 space-y-6">
      <div className="text-center space-y-2">
        <h2 className="text-2xl font-bold">Your Shoe Recommendations</h2>
        <p className="text-muted-foreground">Found {recommendations.length} matching shoes, ranked by relevance</p>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {recommendations.map((shoe, index) => (
          <Card
            key={`${shoe.name}-${shoe.product_code || index}`}
            className="group hover:shadow-hover transition-all duration-300 hover:-translate-y-1 relative overflow-hidden"
          >
            {shoe.rank <= 3 && (
              <div className="absolute top-4 right-4 z-10">
                <Badge variant="default" className="bg-gradient-nike text-white">
                  <Star className="w-3 h-3 mr-1 fill-current" />
                  #{shoe.rank}
                </Badge>
              </div>
            )}
            
            <CardHeader className="pb-3">
              <div className="space-y-2">
                <CardTitle className="text-lg font-bold line-clamp-2">{shoe.name}</CardTitle>
                <p className="text-sm text-muted-foreground">{shoe.category}</p>
                {shoe.size_match && (
                  <Badge variant="secondary" className="w-fit">
                    <Ruler className="w-3 h-3 mr-1" />
                    Size Match
                  </Badge>
                )}
              </div>
            </CardHeader>
            
            <CardContent className="space-y-4">
              <div className="flex items-center justify-between">
                {shoe.price ? (
                  <div className="flex items-center space-x-2">
                    <DollarSign className="w-4 h-4 text-accent" />
                    <span className="font-semibold text-lg">{shoe.price}</span>
                  </div>
                ) : (
                  <span className="text-muted-foreground">Price unavailable</span>
                )}
                
                {shoe.product_code && (
                  <Badge variant="outline" className="text-xs">
                    {shoe.product_code}
                  </Badge>
                )}
              </div>
              
              {shoe.colors && shoe.colors.length > 0 && (
                <div className="space-y-2">
                  <div className="flex items-center space-x-2">
                    <Palette className="w-4 h-4 text-muted-foreground" />
                    <span className="text-sm font-medium">Available Colors:</span>
                  </div>
                  <div className="flex flex-wrap gap-1">
                    {shoe.colors.slice(0, 3).map((color, colorIndex) => (
                      <Badge key={colorIndex} variant="secondary" className="text-xs">
                        {color}
                      </Badge>
                    ))}
                    {shoe.colors.length > 3 && (
                      <Badge variant="secondary" className="text-xs">
                        +{shoe.colors.length - 3} more
                      </Badge>
                    )}
                  </div>
                </div>
              )}
              
              {shoe.sizes && shoe.sizes.length > 0 && (
                <div className="space-y-2">
                  <div className="flex items-center space-x-2">
                    <Ruler className="w-4 h-4 text-muted-foreground" />
                    <span className="text-sm font-medium">Sizes Available:</span>
                  </div>
                  <div className="text-sm text-muted-foreground">
                    {shoe.sizes.length > 5 
                      ? `${shoe.sizes.slice(0, 3).join(", ")} +${shoe.sizes.length - 3} more`
                      : shoe.sizes.join(", ")
                    }
                  </div>
                </div>
              )}
              
              <Button 
                asChild 
                className="w-full bg-primary hover:bg-primary/90 text-primary-foreground transition-all duration-300"
              >
                <a href={shoe.url} target="_blank" rel="noopener noreferrer">
                  View on Nike
                  <ExternalLink className="w-4 h-4 ml-2" />
                </a>
              </Button>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}